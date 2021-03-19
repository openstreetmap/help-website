+++
type = "question"
title = "Why I can&#x27;t add window size as column in Wireshark 1.2.9"
description = '''I am trying to add new column Window size and I can&#x27;t see it in listed columns. I know that in older version it was possible to simply add new column just with right click on the row in packet details. Why it is removed now as an option? Thank you in advance for reply Regards Sanja Petric'''
date = "2013-12-27T06:35:00Z"
lastmod = "2013-12-27T10:09:00Z"
weight = 28438
keywords = [ "columns" ]
aliases = [ "/questions/28438" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why I can't add window size as column in Wireshark 1.2.9](/questions/28438/why-i-cant-add-window-size-as-column-in-wireshark-129)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28438-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28438-score" class="post-score" title="current number of votes">0</div><span id="post-28438-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to add new column Window size and I can't see it in listed columns. I know that in older version it was possible to simply add new column just with right click on the row in packet details. Why it is removed now as an option?</p><p>Thank you in advance for reply</p><p>Regards Sanja Petric</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-columns" rel="tag" title="see questions tagged &#39;columns&#39;">columns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Dec '13, 06:35</strong></p><img src="https://secure.gravatar.com/avatar/a0bacfb7f86038392fe0b16e3509624d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanja%20PM&#39;s gravatar image" /><p><span>Sanja PM</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanja PM has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Dec '13, 14:22</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-28438" class="comments-container"><span id="28440"></span><div id="comment-28440" class="comment"><div id="post-28440-score" class="comment-score"></div><div class="comment-text"><p>The option is not removed but some field haven't got an "apply as column" on purpose. If you give us more detail (such as the field of the protocol you are trying to add column) we can check if it's normal that you can't apply this field as a column. As I know all fields can be applied as a column it's just a code question.</p></div><div id="comment-28440-info" class="comment-info"><span class="comment-age">(27 Dec '13, 07:28)</span> <span class="comment-user userinfo">Afrim</span></div></div><span id="28443"></span><div id="comment-28443" class="comment"><div id="post-28443-score" class="comment-score"></div><div class="comment-text"><blockquote><p>If you give us more detail (such as the field of the protocol</p></blockquote><p>as per the question: 'Window size' which is probably the TCP window size (or calculated window size). Both fields can be added as column by using "apply as column" in 1.10.x and 1.11.x.</p><p><span>@Sanja PM</span>: Please tell us your</p><ul><li>OS and OS version</li><li>Wireshark version</li></ul></div><div id="comment-28443-info" class="comment-info"><span class="comment-age">(27 Dec '13, 08:20)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="28448"></span><div id="comment-28448" class="comment"><div id="post-28448-score" class="comment-score"></div><div class="comment-text"><p>OS is Windows 7 64-bit version. Wireshark version is 1.2.9. Yes it is TCP Window size, and when I click with right button I can't see option Apply as column</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Wireshark_screenshot_small.jpg" alt="alt text" /></p></div><div id="comment-28448-info" class="comment-info"><span class="comment-age">(27 Dec '13, 09:29)</span> <span class="comment-user userinfo">Sanja PM</span></div></div></div><div id="comment-tools-28438" class="comment-tools"></div><div class="clear"></div><div id="comment-28438-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28450"></span>

<div id="answer-container-28450" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28450-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28450-score" class="post-score" title="current number of votes">2</div><span id="post-28450-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="cmaynard has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Wireshark version is 1.2.9.</p></blockquote><p>version 1.2.9 on Windows? Well, that's similar to running Windwos 95 on your PC ;-) How about a more recent version of Wireshark, like 1.10.x or 1.11.x?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Dec '13, 09:47</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span></p></img></div></div><div id="comments-container-28450" class="comments-container"><span id="28451"></span><div id="comment-28451" class="comment"><div id="post-28451-score" class="comment-score"></div><div class="comment-text"><p>Thank you Kurt Knochner. It really helps when you have last version of the software :).</p><p>Regards Sanja PM</p></div><div id="comment-28451-info" class="comment-info"><span class="comment-age">(27 Dec '13, 10:07)</span> <span class="comment-user userinfo">Sanja PM</span></div></div><span id="28452"></span><div id="comment-28452" class="comment"><div id="post-28452-score" class="comment-score"></div><div class="comment-text"><p>Ah yes sorry :)</p></div><div id="comment-28452-info" class="comment-info"><span class="comment-age">(27 Dec '13, 10:09)</span> <span class="comment-user userinfo">Afrim</span></div></div></div><div id="comment-tools-28450" class="comment-tools"></div><div class="clear"></div><div id="comment-28450-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

