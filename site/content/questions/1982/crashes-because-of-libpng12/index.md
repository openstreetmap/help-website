+++
type = "question"
title = "Crashes because of libpng12"
description = '''Wireshark crashes when I try to start it. Console tells me it&#x27;s a problem with libpng12.0.dylib. My searches for fixes for this are turning up fruitless. Can anyone point me in the right direction? Any help is appreciated. Running OSX 10.6.4 . Thanks. 1/28/11 12:50:30 AM defaults[3650]  The domain/d...'''
date = "2011-01-27T22:12:00Z"
lastmod = "2013-03-25T03:26:00Z"
weight = 1982
keywords = [ "macintosh" ]
aliases = [ "/questions/1982" ]
osqa_answers = 5
osqa_accepted = false
+++

<div class="headNormal">

# [Crashes because of libpng12](/questions/1982/crashes-because-of-libpng12)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1982-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark crashes when I try to start it. Console tells me it's a problem with libpng12.0.dylib. My searches for fixes for this are turning up fruitless. Can anyone point me in the right direction? Any help is appreciated. Running OSX 10.6.4 . Thanks.</p><pre><code>1/28/11 12:50:30 AM defaults[3650]  
The domain/default pair of (.GlobalPreferences, AppleCollationOrder) does not exist
1/28/11 12:50:30 AM [0x0-0x8d08d].org.wireshark.Wireshark[3616] dyld: Library not loaded: /usr/X11/lib/libpng12.0.dylib
1/28/11 12:50:30 AM [0x0-0x8d08d].org.wireshark.Wireshark[3616]   Referenced from: /Applications/Wireshark.app/Contents/Resources/bin/wireshark-bin
1/28/11 12:50:30 AM [0x0-0x8d08d].org.wireshark.Wireshark[3616]   Reason: Incompatible library version: wireshark-bin requires version 45.0.0 or later, but libpng12.0.dylib provides version 42.0.0
1/28/11 12:50:31 AM ReportCrash[3661]   Saved crash report for wireshark-bin[3619] version ??? (???) to /Users/jac/Library/Logs/DiagnosticReports/wireshark-bin_2011-01-28-005031_jac.crash</code></pre></div><div id="question-tags" class="tags-container tags">macintosh</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jan '11, 22:12</strong></p><img src="https://secure.gravatar.com/avatar/a4050de6ecca9d62739ebc36c6b986f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rober&#39;s gravatar image" /><p>rober<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rober has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Jan '11, 00:51</p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-1982" class="comments-container"><span id="1994"></span><div id="comment-1994" class="comment"><div id="post-1994-score" class="comment-score"></div><div class="comment-text"><p>I just downloaded wireshark on my new MacBook and I have the same problem.</p></div><div id="comment-1994-info" class="comment-info"><span class="comment-age">(28 Jan '11, 10:47)</span> coolaj86</div></div></div><div id="comment-tools-1982" class="comment-tools"></div><div class="clear"></div><div id="comment-1982-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

5 Answers:

</div>

</div>

<span id="1997"></span>

<div id="answer-container-1997" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1997-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Here's what solved the problem for me:</p><ul><li>ran <code>Software Update...</code></li><li>Rebooted</li><li><a href="http://www.kleinsch.com/2009/10/03/wireshark-chmodbpf-errors-on-snow-leopard/">Changed ChmodBPF permissions</a></li></ul><p>Now it works.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jan '11, 11:10</strong></p><img src="https://secure.gravatar.com/avatar/0a8b345ddcfc5401f578c850442f1e1b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="coolaj86&#39;s gravatar image" /><p>coolaj86<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="coolaj86 has no accepted answers">0%</span></p></div></div><div id="comments-container-1997" class="comments-container"><span id="2006"></span><div id="comment-2006" class="comment"><div id="post-2006-score" class="comment-score"></div><div class="comment-text"><p>It worked. Thanks everyone.</p></div><div id="comment-2006-info" class="comment-info"><span class="comment-age">(29 Jan '11, 00:29)</span> rober</div></div></div><div id="comment-tools-1997" class="comment-tools"></div><div class="clear"></div><div id="comment-1997-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2001"></span>

<div id="answer-container-2001" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2001-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately, the Wireshark builds are not done with the 10.5 or 10.6 SDK, they're done with the libraries that are on the build system, and, equally unfortunately, software updates can introduce libraries with higher "compatibility versions", so that if you build on 10.x.y, the result of the build might expect libraries with the "compatibility versions" from 10.x.y, and 10.x.z, where z &lt; y, might have libraries with earlier "compatibility versions".</p><p>The 10.6 buildbot is currently running 10.6.6, so if you're running an earlier version of 10.6, you might have to do a software update to 10.6.6 in order to run one of the Wireshark builds.</p><p>Changing the permissions on the BPF devices with, for example, ChmodBPF won't affect this; it will just affect whether you can capture with Wireshark once you've gotten Wireshark to start at all.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jan '11, 12:47</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Feb '11, 16:17</p></div></div><div id="comments-container-2001" class="comments-container"><span id="2301"></span><div id="comment-2301" class="comment"><div id="post-2301-score" class="comment-score"></div><div class="comment-text"><p>I've got 10.6.6. When I run wireshark it complaims about an inaddequate libpng library. Specifically:</p><p>2011-02-13 09:22:53.581 defaults[77743:903]</p><p>The domain/default pair of (kCFPreferencesAnyApplication, AppleAquaColorVariant) does not exist 2011-02-13 09:22:53.610 defaults[77744:903]</p><p>The domain/default pair of (kCFPreferencesAnyApplication, AppleHighlightColor) does not exist dyld: Library not loaded: /usr/X11/lib/libpng12.0.dylib</p><p>Referenced from: /Applications/Wireshark.app/Contents/Resources/bin/wireshark-bin Reason: Incompatible library version: wireshark-bin requires version 45.0.0 or later, but libpng12.0.dylib provides version 42.0.0</p></div><div id="comment-2301-info" class="comment-info"><span class="comment-age">(13 Feb '11, 08:24)</span> SGBotsford</div></div><span id="2314"></span><div id="comment-2314" class="comment"><div id="post-2314-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>I have the same problem, I've fixed the ChmodBPF permissions, I have an up to date Mac OS X 10.6.6 (the system tells me no more updates) but I still have this message while launching wireshark :</p><p>MacBook-Pro-de-Yann-Sionneau:~ fallen$ wireshark 2011-02-14 00:08:09.162 defaults[522:903] The domain/default pair of (kCFPreferencesAnyApplication, AppleAquaColorVariant) does not exist 2011-02-14 00:08:09.173 defaults[523:903] The domain/default pair of (kCFPreferencesAnyApplication, AppleHighlightColor) does not exist dyld: Library not loaded: /usr/X11/lib/libpng12.0.dylib Referenced from: /Applications/Wireshark.app/Contents/Resources/bin/wireshark-bin Reason: Incompatible library version: wireshark-bin requires version 45.0.0 or later, but libpng12.0.dylib provides version 42.0.0 Trace/BPT trap</p><p>doing locate libpng gives me : /opt/local/bin/libpng-config /opt/local/bin/libpng14-config /opt/local/include/libpng14 /opt/local/include/libpng14/png.h /opt/local/include/libpng14/pngconf.h /opt/local/lib/libpng.a /opt/local/lib/libpng.dylib /opt/local/lib/libpng.la /opt/local/lib/libpng14.14.dylib /opt/local/lib/libpng14.a /opt/local/lib/libpng14.dylib /opt/local/lib/libpng14.la /usr/X11/bin/libpng-config /usr/X11/bin/libpng12-config /usr/X11/include/libpng12 /usr/X11/include/libpng12/png.h /usr/X11/include/libpng12/pngconf.h /usr/X11/lib/libpng.3.41.0.dylib /usr/X11/lib/libpng.3.44.0.dylib /usr/X11/lib/libpng.3.dylib /usr/X11/lib/libpng.dylib /usr/X11/lib/libpng12.0.41.0.dylib /usr/X11/lib/libpng12.0.44.0.dylib /usr/X11/lib/libpng12.0.dylib /usr/X11/lib/libpng12.dylib</p></div><div id="comment-2314-info" class="comment-info"><span class="comment-age">(13 Feb '11, 16:12)</span> yannsionneau</div></div><span id="2328"></span><div id="comment-2328" class="comment"><div id="post-2328-score" class="comment-score"></div><div class="comment-text"><p>For people who've updated to 10.6.6 but still have this problem:</p><ol><li><p>what does the command "sw_vers" print?</p></li><li><p>did you install X11 when you first got the machine, or later, possibly after doing an update?</p></li></ol></div><div id="comment-2328-info" class="comment-info"><span class="comment-age">(14 Feb '11, 10:23)</span> Guy Harris ♦♦</div></div><span id="2358"></span><div id="comment-2358" class="comment"><div id="post-2358-score" class="comment-score">1</div><div class="comment-text"><p>sw_vers ProductName: Mac OS X ProductVersion: 10.6.6 BuildVersion: 10J567</p><p>I re-installed X11 today.</p><p>After fighting this identical problem for awhile, I ran 'sudo port install wireshark-devel', started from the command line, and it is now working for me.</p></div><div id="comment-2358-info" class="comment-info"><span class="comment-age">(15 Feb '11, 21:09)</span> mbaugher</div></div></div><div id="comment-tools-2001" class="comment-tools"></div><div class="clear"></div><div id="comment-2001-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6364"></span>

<div id="answer-container-6364" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6364-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I had the same problem exactly as described. I downloaded the latest version of x11 from Apple. Turns out I already had it. So following various hints I found and downloaded the current version of xQuartz. I logged off and back on... no joy. So I downloaded and installed IncScape as recommended somewhere. IncScape ran fine but not WireShark.</p><p>Doing printenv to check the DISPLAY variable I glanced at the PATH variable. So there is a /opt/X11/lib in the path followed by the /usr/X11/lib. I had looked at the /usr/X11/lib after each of the above installs and there were no changes so I decided to look to see if the xQuartz libraries were in /opt/ and they were.</p><p>It appears that the version of WireShark I have 1.6.1 has /usr/X11/lib hardcoded. I deleted this library and copied the library from /opt/X11 into /usr/ and it works now.</p><p>I have ignored this problem for about a year and perhaps I should have got the most recent version of Wireshark which may have fixed this but I'm posting this anyway in case there are any other stubborn folks out there.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '11, 08:59</strong></p><img src="https://secure.gravatar.com/avatar/203626a419f989154aceb0d7a374b4bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tolinski&#39;s gravatar image" /><p>tolinski<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tolinski has no accepted answers">0%</span></p></div></div><div id="comments-container-6364" class="comments-container"></div><div id="comment-tools-6364" class="comment-tools"></div><div class="clear"></div><div id="comment-6364-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18672"></span>

<div id="answer-container-18672" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18672-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I had the same problem with 10.7.5. Running '<strong>sudo port install wireshark-devel</strong>'fixed the problem. Well, I say 'fixed' - Wireshark won't launch from the desktop, but if I start it in a terminal window, it runs fine. Seems I was missing most of the glib packages, which I've never been able to successfully install before now, using either port or fink. Hope this is helpful to others with the same problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Feb '13, 18:47</strong></p><img src="https://secure.gravatar.com/avatar/ccf5f51cca6f8f4817e75a210182804f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cephas&#39;s gravatar image" /><p>Cephas<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cephas has no accepted answers">0%</span></p></div></div><div id="comments-container-18672" class="comments-container"></div><div id="comment-tools-18672" class="comment-tools"></div><div class="clear"></div><div id="comment-18672-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19799"></span>

<div id="answer-container-19799" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19799-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As everyone in here I experiment Wireshark crashes at start. I must say taht I'm running OSX 10.5.8 first. To solve the problem, I install Quartz 2.6.3 and WireShark 1.8.6. WS take a little while to start, but it works fine.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '13, 03:26</strong></p><img src="https://secure.gravatar.com/avatar/f413f1d8d63599321713607a0b783c78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Simon&#39;s gravatar image" /><p>Simon<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Simon has no accepted answers">0%</span></p></div></div><div id="comments-container-19799" class="comments-container"></div><div id="comment-tools-19799" class="comment-tools"></div><div class="clear"></div><div id="comment-19799-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

