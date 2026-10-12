# Magic Caster Wand — web app + HD effects pack

This folder is a complete website:

- `index.html` — the app
- `effects/` — 20 HD spell-effect videos (1080×1080 MP4, black background) and `manifest.json`

## Start here

1. Open the app and tap **Check my wand** on the Cast tab (also available in Learning & practice).
2. Wake your wand, close the official app on other devices, then connect. Both **Defiant** and **Honorable** use the shared Magic Caster Wand protocol. Automatic detection is the default; the model selector provides a fallback when the device does not identify itself.
3. Follow the connection, light, vibration and casting checks. The app verifies the connection and incoming wand spell messages. Confirm light and vibration only when you see or feel them on your physical wand. A successful command write alone does not mean the hardware worked.
4. In **Learning & practice → Getting started**, learn **Lumos**, then try the one-minute **Snitch Chase** game. Choose wand-tip controls or touch. Camera access is used for wand-tip tracking; recording can be turned off in Games.
5. Explore Spells for more gestures, Learning & practice for lessons, and the Great Hall for full-screen shows.

Light-check choices are remembered separately for each paired wand. Connecting a new wand starts with the proven direct-light command. Only one wand is connected at a time.

Protocol reference: [hass-magic-caster-wand BLE client](https://github.com/eigger/hass-magic-caster-wand/blob/master/custom_components/magic_caster_wand/mcw_ble/mcw.py).

If the connection drops, the app retries automatically. Keep the wand close, wake it and close competing apps. If retries stop, tap the wand badge or Reconnect. **Settings → Copy Bluetooth report** includes model, identity, firmware, command-channel availability and recent errors for troubleshooting.

## Verification

The project includes `../tests/protocol.test.cjs` and `../tests/browser.cjs`.

`../tests/effects.cjs` checks every effect preset, distinct spell layers, repeated-cast cleanup, reduced motion, video races, real bundled video playback and mobile limits. `../tests/actions.cjs` checks saved mapping retention, edit, pause/resume, validation, file replacement, remove/undo and responsive layouts. Run these with Playwright and installed Chrome available to Node.

Run `node --test tests/protocol.test.cjs` from the project root. The browser regression check requires Playwright and installed Google Chrome; run `node tests/browser.cjs` with Playwright available to Node.

The browser checks simulate Bluetooth devices: Honorable/Defiant switching, stale commands, old notifications, small-packet fallback, repeated spell-button use, guided confirmations, remembered devices and first-time navigation. They do **not** certify physical wand operation. Run Check my wand with each actual wand to verify lights, vibration and casting.

The standalone `../Magic Caster Wand.html` mirrors this app. `../MagicCasterWand-upload.zip` contains this website and its effects. The older `../magic-wand-web (improved).html` is a legacy version and has not been updated.

## Media player

Open **Media → Offline videos** in the bottom bar and choose **Add videos**, or drop files into the player. Files stay on your device and must be added again after reload. Play/pause, Stop, ±10-second seeking, timeline, volume, speed and fullscreen are available. The playlist moves to the next video when one ends.

Connect your wand in Cast, return to Media and enable **Wand remote**. Default spells are **Lumos** (play/pause), **Immobulus** (pause), **Nox** (stop and return to start), **Accio** (forward 10s) and **Depulso** (rewind 10s). Change them in the dropdowns; assigning a spell already in use swaps the two controls. Wand media commands apply only in Media and replace spell effects and saved actions there. Leaving the tab pauses the video. If your browser blocks a wand-triggered Play, tap Play once first.

MP4, WebM, Ogg, MOV and other video containers can be added. Actual playback depends on the codecs inside the file and the browser; MKV, AVI and WMV may fail. H.264/AAC MP4 is a useful fallback. The app shows format hints and errors; it does not convert files. See [MDN’s media container guide](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Containers).

`../tests/media.cjs` requires Playwright, installed Chrome and ffmpeg. It generates disposable test videos and checks playback, wand packet routing, seeking, playlists, preference storage, unsupported-file recovery, URL cleanup and mobile layouts.

## Browser retired

The Browser tab has been removed from navigation. Its sandboxed implementation is retained internally for recovery and regression checks.

## Online IPTV

Open **Media → Online TV**, choose a playlist, and tap **Load channels**. These public playlists are provided by [iptv-org on GitHub](https://github.com/iptv-org/iptv). Search by channel name or filter by category, then tap a channel. Lists are fetched on demand; availability changes over time.

Expand **Your playlist or stream** to load an HTTP/HTTPS M3U playlist, a direct HLS stream URL, or import an M3U file. Relative channel links use the playlist URL as their base. URLs and catalogs remain in the current session and are not saved to localStorage. Native HLS playback is used when available, with bundled [HLS.js 1.7.3](https://github.com/video-dev/hls.js/releases/tag/v1.7.3) as a fallback. Third-party license files are included.

Wand controls also work for streams. **Flipendo** chooses the next channel and **Reparo** the previous channel (within the current search/category list). The mapping dropdowns can change these spells. **Lumos** plays/pauses, **Immobulus** pauses and **Nox** stops. Accio/Depulso seek within the channel’s rewind buffer when one exists; a live channel cannot always seek like a local movie.

Some channels are offline, region-restricted or disallow browser access through CORS. HTTP streams are blocked on an HTTPS page. The app reports stream failures, offers Retry stream and lets you switch channels. It does not proxy streams, supply subscription credentials, bypass restrictions or support DRM-only TV services.

`../tests/iptv.cjs` verifies real HLS playback using a temporary local CORS-enabled stream, plus playlist parsing/import, filtering, request races, errors, cleanup and wand controls. A separate live browser check loaded the public News list and played France 24 English successfully; this does not certify every listed channel. Physical wand behavior remains unverified.

## Two new games

**Potion Mix**: remember the ingredient pictures, then point at them in order. Hold briefly to select; move away between picks. A wrong ingredient shows the recipe again. Complete recipes for bonus points.

**Star Trail**: point at each numbered glowing star in order to draw a constellation. Complete paths for bonus points. Both games last one minute and work with camera-tracked wand-tip controls or touch/mouse. Camera access and a visible glowing tip are needed for wand controls; touch works without a camera. Recording is optional.

`../tests/games.cjs` checks input, scoring, retries, results, restarting and camera cleanup.

## Improved visuals and controls

The spell renderer is shared by Honorable and Defiant. In Spells, open **Try the spell effects** to preview eight key effects without activating your wand or saved actions. The existing video pack can be combined with procedural effects; videos keep their full aspect ratio on phones and PCs. Reduced-motion preferences use a short stationary glow instead of moving particles and video.

Cast begins with **Start here**: connect your wand, listen for spells and enter the Great Hall. **Ways to cast** and **Wand & box settings** follow. Connecting a wand starts spell listening after connection succeeds; you can stop it with **Stop listening**. Pairing settings, box controls and light controls are expandable. Actions has a spell/action editor and a saved-action list. Use Edit, Test, Pause/Resume or Remove; removal offers Undo. Quick Launch has been removed. Primary instructions use icons, short labels and visual progress; detailed action help is expandable.

These visuals improve the existing resources rather than exactly replicate official wand effects. Exact matching would require reference footage. Confirm actual light, vibration and casting behavior using your physical wand.

## Put it online (needed for phones and for the "Download HD effects" button)

Bluetooth, camera and microphone require a secure address such as HTTPS or localhost, and the in-app download fetches `effects/` from the same address.

**Fastest — Netlify Drop (free, about 1 minute):**
1. Go to https://app.netlify.com/drop
2. Drag this whole folder onto the page.
3. Open the `https://….netlify.app` link it gives you, on your phone or PC.
4. In the app, tap **Download HD effects (28 MB)**.

Sign up for a free Netlify account to keep the link permanently.

**GitHub Pages (free):**
1. Create a public repository, e.g. `magic-caster-wand`.
2. Upload everything in this folder (including `effects/` and the `.nojekyll` file).
3. In the repository, go to Settings → Pages → Deploy from branch → `main` / root.
4. Open `https://<your-username>.github.io/magic-caster-wand/`.

## Using it offline from the file

Open `index.html` directly in Chrome or Edge. Then go to Settings → Spell effects → **Install from files** and select every `.mp4` in `effects/`.

## Separate offline and online players

Media has two independent players: **Offline videos** for local files and **Online TV** for streams. Each keeps its own queue, volume, playback speed and wand assignments. Switching pauses the previous player without deleting its queue; wand commands go to the selected player. Clearing either queue leaves the other alone.

Online TV offers 12 on-demand GitHub-hosted playlists: News, Movies, Music, Sports, Kids, Documentary, Pakistan, India, United States, United Kingdom, English and Urdu. Choose a preset and tap **Load channels**, or open **GitHub playlist links** to load an individual list or open its URL. Sources: [iptv-org playlist catalog](https://github.com/iptv-org/iptv/blob/master/PLAYLISTS.md). Playlist availability does not guarantee every channel will play in a browser.

## Reliable wand input and microphone sessions

For local use, double-click **Start Magic Wand.command** (Python 3 required). It opens Google Chrome at **http://localhost:8765/** and serves only on this computer. Keep the launcher window open; Ctrl+C stops it. A consistent localhost address gives the browser a stable site for permissions. Reconnect the wand on this address; permissions and saved settings belong to each browser origin.

Recognized Bluetooth wand spells cast immediately, including when Combo mode or voice listening is selected. Smart/Combo camera and voice behavior remains available. Media and Browser route wand spells to their selected remote; Games route to the active game; Great Hall and WandCheck take casting priority.

Games offer **Connected wand**, **Wand tip** (camera), and **Touch**. All game control modes keep the camera view and track the glowing wand tip. Connected spell controls also work; microphone is optional. Potion: Lumos chooses leaf, Accio chooses mushroom, Protego chooses crystal. Stars: Lumos/Accio advances one star; Reparo restarts the current constellation. Duel: cast the displayed spell. Snitch: Accio summons it. Defence: Expecto Patronum, Lumos and Protego. Mirror: any spell.

Microphone recording is opt-in; game video recording is on by default. Tap **Listen** in Cast, the floating dock, a game or Great Hall; Browser has its own voice buttons. After an explicit Listen tap, speech recognition stays enabled across tabs and restarts on normal session endings. Denied permissions, missing microphones and repeated network errors stop listening rather than opening a prompt loop. Browser voice typing temporarily pauses spell recognition and restores it afterwards. Entering Great Hall or successfully connecting a wand starts spell listening. Opening a game preserves existing listening; its Listen button can start or stop it. Older microphone recording settings are switched off once during migration, and a separate migration restores default game video recording. Users can change either recording option. The app cannot override browser/OS permission policies, especially on file URLs.

## Academy and continuous listening

The new **Academy** tab teaches eight basic spells with syllable and stress guides, slow browser-spoken examples, visual demonstrations, voice/wand practice and saved completion. A demonstration does not count as a learned spell. Recognition feedback identifies a different spell or suggests the selected pronunciation; it is not a measurement of accent or pronunciation quality. The [official grip tutorial](https://checkout.harrypottermagiccasterwand.com/pages/set-up-your-magic-caster-wand) explains holding and releasing the wand.

Tap **Start listening** once in the voice bar to listen across the app, then **Stop listening** when finished. On localhost/HTTPS, normal speech-session endings restart with a short delay. Permission denial and audio errors stop immediately; three consecutive network failures stop retries. Browser dictation owns the microphone temporarily, then resumes spell listening. After reload, use Listen, enter Great Hall or reconnect the wand to start recognition. Hidden/suspended browsers may pause capture; foregrounding resumes a requested session. File URLs retain explicit-session behavior to prevent permission loops. Audio recognition and voice availability depend on the browser and its speech service.

Voice matching prioritizes complete spell names and pronunciation aliases, requires a clear winner for fuzzy matches, and rejects short approximate words. Longer incantations win over their prefixes. App-generated pronunciation audio is muted out of detection. No microphone recordings or transcripts are saved by this feature; lesson completion is saved locally.

Device firmware is unchanged. The repository has firmware-version reporting but no verified firmware package or supported firmware flashing path. These improvements run in the web app.

Game recording is on by default. Finishing or leaving a recorded game opens the clip with Download and Share, and saves it in My videos. Record my voice remains a separate optional setting. Game scenes keep the tip light steady; camera tracking accepts compact bright white or coloured tips.

### Retained destruction games (removed from launch cards)

**Crystal Sling** is portrait; **Castle Cannon** is landscape. Aim with the wand tip or touch, then squeeze and release or cast **Accio**. You can also use the **Fire** button. **Reparo** / **Retry** restarts the current level and rolls back that level’s score. Shatter every crystal with up to six shots to advance. Explosive barrels damage nearby towers. Adjust the **Power** slider; on a keyboard, arrows adjust angle/power, Space fires and R retries. Both games retain camera video and downloadable recordings.

The Great Hall starts listening when entered. Its persistent panel shows connection state and any words the browser actually reports. The wand must be connected to the current app tab; reloading requires reconnecting. Recording video and recording your microphone are separate settings.

## Home screen and drawing guides

**Cast → Start here** has three steps. **Your wand** shows whether this tab is connected. **Say a spell** shows the microphone state, the words the browser heard, the spell it recognised and your last completed cast. **Great Hall** opens the full-screen show. Only one browser tab can hold the wand; close other app tabs and the official app if connecting fails.

Tap any spell in Spells, Academy, Actions, Learn or the home shortcuts to see its drawing guide. **With your wand** shows the wand gesture picture: squeeze, start at the round dot, follow the arrows in one stroke and release. The picture needs an internet connection. **Camera mode** appears for the nine camera spells: start at the white dot and follow the arrows. **Hear** speaks the pronunciation. Spells with no mapped gesture say "Drawing guide not yet available"; cast them with your voice.

In the Great Hall, the status panel, Listen and Leave stay above spell effects. When this tab has no wand, the Hall offers **Connect wand**.

`../tests/home-guides.cjs` checks the home states, every spell guide, guide shapes traced in Spell Duel, Great Hall controls during effects, layouts from 320 to 1280 px and reduced motion. Its speech, camera and Bluetooth are simulated.

## Simpler experience and light shows

Cast has Rainbow Journey, Northern Lights and Golden Welcome shows, plus Random Show and Stop. Connect wand and box to send matching short colour commands to both; Bluetooth timing may vary. Magical chimes or a chosen audio file play through the phone/computer or its speaker, not the box. The box's built-in opening theme is separate. Shows stop on navigation, casting, game entry and when the app is hidden.

Learn and Academy are combined in a learning area accessible from Cast and Spells. Practice in Great Hall saves completed lessons from real voice/wand casts; demonstrations do not count. Casting defaults to wand or voice; no mode selection is needed.

Games start with Snitch Chase, Dementor Defence and Spell Duel. Crystal Sling and Castle Cannon are removed from launch cards, retaining saved clips and their implementations. Spell Duel accepts the spoken target as well as a gesture. Every launch card opens lighting/positioning guidance and an optional live tracking check with sensitivity adjustment. Camera, recording, downloads and sharing remain available.

The tracker detects compact bright coloured/white tips and rejects broad bright regions. Tiny lamps can still resemble tips; real hardware validation is needed. There is no universal camera distance or perfect-tracking guarantee.

## Balloon Pop, Rune Hunt and Professor Ember

**Balloon Pop:** point your glowing tip (or finger) at a balloon until it pops. Golden balloons are worth more, and the waves get breezier and busier. Missing a balloon only ends your combo. Casting **Bombarda** pops every balloon on screen, then recharges for 15 seconds.

**Rune Hunt:** hold your tip on a rune until its ring fills. Rounds switch between drifting runes, orbiting runes and numbered runes caught in order for a bonus. Casting **Lumos** or **Revelio** slows the runes for a few seconds.

Both games start with the usual tracking check, keep the camera on and save recordings like the other games.

**Professor Ember** is a built-in guide, not a real person. Tap the little ember in the header for a tip. **Show me** points at the right control, **Got it** dismisses a tip and ✕ hides Ember. Tips can be read aloud with the speaker button; the app ignores Ember's voice while listening for spells. Turn Ember or its voice off in **Settings → Casting**.

If the voice status says **No sound heard**, check that your microphone isn't muted and that the right microphone is selected.

## More spell actions

**Actions** now offers 31 things a spell can do, in groups: wand & box lights and shows, magic effects and sounds, app shortcuts (Great Hall, a game, a page), a magic timer, saying the time, and **Stop everything**. Under the action picker you'll see what it does. Open **ⓘ What you need & tips** to see whether your wand, box or browser is ready, use the suggested spell, or tap **Try it now** to test it before saving. Saved actions show ⚠ when something they need, like a connected wand, is missing.

