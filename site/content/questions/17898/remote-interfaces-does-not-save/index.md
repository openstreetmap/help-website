+++
type = "question"
title = "Remote Interfaces does not save."
description = '''Hi All, I have successfully configured remote interfaces using rpcdap on remote Linux server from my windows machine. However I have notice that once I configure the remote interfaces when I close wireshark and reopen it it disappears. Is there a way to save this configuration as I have multiple ser...'''
date = "2013-01-23T07:22:00Z"
lastmod = "2013-01-23T17:07:00Z"
weight = 17898
keywords = [ "interface", "to", "unable", "remote", "save" ]
aliases = [ "/questions/17898" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Remote Interfaces does not save.](/questions/17898/remote-interfaces-does-not-save)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17898-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I have successfully configured remote interfaces using rpcdap on remote Linux server from my windows machine. However I have notice that once I configure the remote interfaces when I close wireshark and reopen it it disappears. Is there a way to save this configuration as I have multiple servers and would hate to input them every time.</p><p>I know from the wireshark documentation it states for remote interfaces that "In contrast to the local interfaces they are not saved in the "Preferences" file". I was hoping that there might be some other file it should be saved in or a hack of sorts.</p><p>Thanks in advance, Jordan</p></div><div id="question-tags" class="tags-container tags">interface to unable remote save</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jan '13, 07:22</strong></p><img src="https://secure.gravatar.com/avatar/148910925713fb44527dd62357e363ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jsmolar&#39;s gravatar image" /><p>jsmolar<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jsmolar has no accepted answers">0%</span></p></div></div><div id="comments-container-17898" class="comments-container"></div><div id="comment-tools-17898" class="comment-tools"></div><div class="clear"></div><div id="comment-17898-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17915"></span>

<div id="answer-container-17915" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17915-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately, no, there's no file that they're saved in.</p><p>They should probably be saved transparently in the "recent" file, rather than as an explicitly-saved preference. Please file a request for enhancement at <a href="http://bugs.wireshark.org/">the Wireshark bugzilla</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jan '13, 17:07</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-17915" class="comments-container"><span id="18402"></span><div id="comment-18402" class="comment"><div id="post-18402-score" class="comment-score"></div><div class="comment-text"><p>But I remember that in old versions the configured remote interfaces did not vanish.</p></div><div id="comment-18402-info" class="comment-info"><span class="comment-age">(07 Feb '13, 06:44)</span> Wire-Rob</div></div><span id="56738"></span><div id="comment-56738" class="comment"><div id="post-56738-score" class="comment-score"></div><div class="comment-text"><p>No need for another bug; this request is already tracked as <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8557">bug 8557</a>.</p></div><div id="comment-56738-info" class="comment-info"><span class="comment-age">(27 Oct '16, 06:34)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-17915" class="comment-tools"></div><div class="clear"></div><div id="comment-17915-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

