+++
type = "question"
title = "Has anyone used Wireshark to troubleshoot ICEfaces?"
description = '''I am in the process of troubleshooting a latency issue. The application is written using ICEfaces and is using SSO. I am wondering if there is a better filter to use other than ip.addr of the workstation and server. I can see a lot of pauses between packets coming from the server. I am not sure if t...'''
date = "2013-12-21T12:36:00Z"
lastmod = "2013-12-21T15:40:00Z"
weight = 28315
keywords = [ "sso", "java", "icefaces" ]
aliases = [ "/questions/28315" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Has anyone used Wireshark to troubleshoot ICEfaces?](/questions/28315/has-anyone-used-wireshark-to-troubleshoot-icefaces)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28315-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am in the process of troubleshooting a latency issue. The application is written using ICEfaces and is using SSO. I am wondering if there is a better filter to use other than ip.addr of the workstation and server. I can see a lot of pauses between packets coming from the server. I am not sure if this is due to lack of user input or actual slowness of the server to respond.</p></div><div id="question-tags" class="tags-container tags">sso java icefaces</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Dec '13, 12:36</strong></p><img src="https://secure.gravatar.com/avatar/5b20990cd21bd091665e684410ebe9fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdJ&#39;s gravatar image" /><p>EdJ<br />
<span class="score" title="16 reputation points">16</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdJ has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Dec '13, 12:38</p></div></div><div id="comments-container-28315" class="comments-container"></div><div id="comment-tools-28315" class="comment-tools"></div><div class="clear"></div><div id="comment-28315-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28318"></span>

<div id="answer-container-28318" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28318-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you wonder what the user is doing you should do a capture while watching &amp; documenting what he IS doing. That is usually the best way to stop wondering if a delay is based on a human or a machine delay.</p><p>Packets coming from the server should usually come without delay, because users are usually not on the server but on the client, and the server has to process incoming requests as fast as possible. To determine that you need to capture as close to the server as possible, because otherwise you'd be guessing if there is also network transport delay.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Dec '13, 15:40</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-28318" class="comments-container"></div><div id="comment-tools-28318" class="comment-tools"></div><div class="clear"></div><div id="comment-28318-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

