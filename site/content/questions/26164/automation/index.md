+++
type = "question"
title = "Automation"
description = '''Hi, We have wireshark in our lab. We have encoders,set boxes in our company and we used capture the packets using UDP multicast. We are trying to automate T-shark using AutoIT Language?  Tshark –V –R “ip.addr == 233.1.1.202” –i 1 –c 1 Do you have any idea on T-shark Automation? is it possible?'''
date = "2013-10-18T03:47:00Z"
lastmod = "2013-10-18T10:01:00Z"
weight = 26164
keywords = [ "wireshark" ]
aliases = [ "/questions/26164" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Automation](/questions/26164/automation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26164-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>We have wireshark in our lab. We have encoders,set boxes in our company and we used capture the packets using UDP multicast.</p><p>We are trying to automate T-shark using AutoIT Language?  Tshark –V –R “ip.addr == 233.1.1.202” –i 1 –c 1</p><p>Do you have any idea on T-shark Automation? is it possible?</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Oct '13, 03:47</strong></p><img src="https://secure.gravatar.com/avatar/070b08ccd78becfd46743bd1421c6e12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vaish&#39;s gravatar image" /><p>vaish<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vaish has no accepted answers">0%</span></p></div></div><div id="comments-container-26164" class="comments-container"><span id="26177"></span><div id="comment-26177" class="comment"><div id="post-26177-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Do you have any idea on T-shark Automation? is it possible?</p></blockquote><p>For sure it is possible to automate tshark with AutoIT. However, I don't understand what you are trying to do and what kind of problem you ran into with AutoIT?</p><p>Can you please add more details?</p><p>Regards<br />
Kurt</p></div><div id="comment-26177-info" class="comment-info"><span class="comment-age">(18 Oct '13, 09:49)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-26164" class="comment-tools"></div><div class="clear"></div><div id="comment-26164-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26180"></span>

<div id="answer-container-26180" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26180-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you running <code>tshark</code> with that <em>exact</em> command line? If so you're delimiting each flag with a Unicode EN DASH (U+2013) instead of a plain old regular HYPHEN-MINUS (U+002D). Here's what hexdump returns when I feed it one of the dashes above:</p><pre><code>$ echo -n – | hexdump
0000000 e2 80 93                                       
0000003</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '13, 10:01</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span> </br></p></div></div><div id="comments-container-26180" class="comments-container"></div><div id="comment-tools-26180" class="comment-tools"></div><div class="clear"></div><div id="comment-26180-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

