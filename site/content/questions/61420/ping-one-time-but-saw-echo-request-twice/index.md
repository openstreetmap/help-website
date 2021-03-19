+++
type = "question"
title = "ping one time but saw echo request twice"
description = '''I use command ping 192.168.2.10 -n 1 to test net connection in windows cmd. Simultaneous use wireshark to see what happend. As I think there should be a echo request and a echo replay,but actually saw two echo request and one echo replay,lieke this:  The first request shows &quot;no response found&quot; and s...'''
date = "2017-05-16T01:02:00Z"
lastmod = "2017-05-16T01:02:00Z"
weight = 61420
keywords = [ "ping" ]
aliases = [ "/questions/61420" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ping one time but saw echo request twice](/questions/61420/ping-one-time-but-saw-echo-request-twice)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61420-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I use command <code>ping 192.168.2.10 -n 1</code> to test net connection in windows cmd. Simultaneous use wireshark to see what happend. As I think there should be a echo request and a echo replay,but actually saw two echo request and one echo replay,lieke this:</p><p><img src="https://raw.githubusercontent.com/oska874/photo-repo/master/a1.png" alt="alt text" /></p><p>The first request shows "no response found" and second shows "reply in 338", while in cmd.exe ping shows ok:</p><p><img src="https://raw.githubusercontent.com/oska874/photo-repo/master/a2.png" alt="alt text" /></p><p>How does this happened?</p><p>environment:</p><pre><code>win10 64bit + wireshark 2.26</code></pre><p>append:</p><p>I tried in Linux with the samee version wireshark and it shows only one request and one reply. So I think it should related to my PC, but I don't know what is the reason ???</p></div><div id="question-tags" class="tags-container tags">ping</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 May '17, 01:02</strong></p><img src="https://secure.gravatar.com/avatar/61dc3268d24f691dcb8c7f727dc4a86d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="oska874&#39;s gravatar image" /><p>oska874<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="oska874 has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 16 May '17, 19:33</p></div></div><div id="comments-container-61420" class="comments-container"><span id="61436"></span><div id="comment-61436" class="comment"><div id="post-61436-score" class="comment-score"></div><div class="comment-text"><p>I've tried to recreate this myself but have been unable to do so with Windows 10 version 1703 (OS Build 15063.296)</p></div><div id="comment-61436-info" class="comment-info"><span class="comment-age">(16 May '17, 08:17)</span> dbAtAffirmed</div></div><span id="61437"></span><div id="comment-61437" class="comment"><div id="post-61437-score" class="comment-score"></div><div class="comment-text"><p>Can you upload the corresponding PCAP?</p></div><div id="comment-61437-info" class="comment-info"><span class="comment-age">(16 May '17, 08:34)</span> dkomna</div></div><span id="61497"></span><div id="comment-61497" class="comment"><div id="post-61497-score" class="comment-score"></div><div class="comment-text"><p>Select one of therequests and have alook in the Packketdetail pane and expand the frame section. There is an attribut called interface. Does it show in both requests the same value?</p></div><div id="comment-61497-info" class="comment-info"><span class="comment-age">(18 May '17, 13:30)</span> Christian_R</div></div></div><div id="comment-tools-61420" class="comment-tools"></div><div class="clear"></div><div id="comment-61420-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

