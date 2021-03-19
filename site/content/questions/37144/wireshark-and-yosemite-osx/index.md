+++
type = "question"
title = "Wireshark and Yosemite OSX"
description = '''I have read the other post concerning Wireshark and Yosemite OSX. I have a similar problem which Wireshark not loading. However, the recommendation are not working. Attached is the error I am seeing when I run from terminal. PapaMac$ sudo wireshark Password: 2014-10-17 20:30:51.763 defaults[1190:246...'''
date = "2014-10-17T19:41:00Z"
lastmod = "2014-10-17T19:41:00Z"
weight = 37144
keywords = [ "yosemite" ]
aliases = [ "/questions/37144" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark and Yosemite OSX](/questions/37144/wireshark-and-yosemite-osx)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37144-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have read the other post concerning Wireshark and Yosemite OSX. I have a similar problem which Wireshark not loading. However, the recommendation are not working. Attached is the error I am seeing when I run from terminal.</p><pre><code>PapaMac$ sudo wireshark
Password:
2014-10-17 20:30:51.763 defaults[1190:246204] The domain/default pair of (kCFPreferencesAnyApplication, AppleAquaColorVariant) does not exist
2014-10-17 20:30:51.807 defaults[1191:246211] The domain/default pair of (kCFPreferencesAnyApplication, AppleHighlightColor) does not exist

(process:1180): Gtk-WARNING **: Locale not supported by C library.
    Using the fallback &#39;C&#39; locale.

(wireshark-bin:1180): Gtk-WARNING **: cannot open display:</code></pre><p>Thanks to all.</p></div><div id="question-tags" class="tags-container tags">yosemite</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Oct '14, 19:41</strong></p><img src="https://secure.gravatar.com/avatar/ac49020a103a5fc94c8fb41069b98364?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JohnRutl&#39;s gravatar image" /><p>JohnRutl<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JohnRutl has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Oct '14, 00:49</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-37144" class="comments-container"><span id="37145"></span><div id="comment-37145" class="comment"><div id="post-37145-score" class="comment-score">1</div><div class="comment-text"><p>What happens if you try to do</p><pre><code>sudo xterm</code></pre><p>and what happens if you try to do</p><pre><code>xterm</code></pre><p>(without the <code>sudo</code>) and what happens if you try to do</p><pre><code>wireshark</code></pre><p>(without the <code>sudo</code>)?</p></div><div id="comment-37145-info" class="comment-info"><span class="comment-age">(18 Oct '14, 00:50)</span> Guy Harris ♦♦</div></div><span id="37148"></span><div id="comment-37148" class="comment"><div id="post-37148-score" class="comment-score">1</div><div class="comment-text"><p>I had the same issue with the actual Yosemite rollout. I uninstalled both X11 and Wireshark from my new install. I then installed X11 and Wireshark in that order. It all works now and seems to be stable. I hope this helps for you.</p></div><div id="comment-37148-info" class="comment-info"><span class="comment-age">(18 Oct '14, 04:39)</span> dotnetbrett</div></div><span id="37214"></span><div id="comment-37214" class="comment"><div id="post-37214-score" class="comment-score"></div><div class="comment-text"><p>Since the update of Yosemite Wireshark appear to work OK. thanks again.</p></div><div id="comment-37214-info" class="comment-info"><span class="comment-age">(20 Oct '14, 19:13)</span> JohnRutl</div></div></div><div id="comment-tools-37144" class="comment-tools"></div><div class="clear"></div><div id="comment-37144-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

