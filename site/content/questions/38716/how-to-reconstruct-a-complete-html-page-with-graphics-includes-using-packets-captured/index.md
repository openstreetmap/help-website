+++
type = "question"
title = "how to reconstruct a complete HTML page with graphics includes using packets captured"
description = '''Need to reconstruct the complete webpage included all GUI'''
date = "2014-12-26T06:49:00Z"
lastmod = "2014-12-27T07:07:00Z"
weight = 38716
keywords = [ "http", "reconstruction", "wireshark" ]
aliases = [ "/questions/38716" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to reconstruct a complete HTML page with graphics includes using packets captured](/questions/38716/how-to-reconstruct-a-complete-html-page-with-graphics-includes-using-packets-captured)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38716-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Need to reconstruct the complete webpage included all GUI</p></div><div id="question-tags" class="tags-container tags">http reconstruction wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Dec '14, 06:49</strong></p><img src="https://secure.gravatar.com/avatar/068262749ef0dbb7458f4502e9c3a436?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wiresharker&#39;s gravatar image" /><p>Wiresharker<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wiresharker has no accepted answers">0%</span></p></div></div><div id="comments-container-38716" class="comments-container"></div><div id="comment-tools-38716" class="comment-tools"></div><div class="clear"></div><div id="comment-38716-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38731"></span>

<div id="answer-container-38731" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38731-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>you can do that with Wireshark, but it would require a lot of manual work. If you need that feature, you could implement it yourself (and donate to code to the project) or file an enhancement bug at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> and hope someone likes it and implements it for you.</p><p>Alternatively you can use a tool that is able to do that right now, like <a href="http://www.xplico.org/">Xplico</a>.</p><blockquote><p><a href="http://www.xplico.org/">http://www.xplico.org/</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Dec '14, 07:07</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-38731" class="comments-container"><span id="38802"></span><div id="comment-38802" class="comment"><div id="post-38802-score" class="comment-score">1</div><div class="comment-text"><p>I know there are many other tools can do that, but I'm just trying to use wireshark to do that. Now I can either reconstruct the html page without images or get the image from the page by using the method File - Export object - HTTP - save the target webpage or image</p><p>But I cannot reconstruct the completed one (the page with text and images). Do you have any suggestion?</p></div><div id="comment-38802-info" class="comment-info"><span class="comment-age">(30 Dec '14, 10:43)</span> Wiresharker</div></div><span id="38808"></span><div id="comment-38808" class="comment"><div id="post-38808-score" class="comment-score"></div><div class="comment-text"><ul><li>Extract the HTML code</li><li>Extract the images</li><li>Save everything in a local directory</li><li>Edit the saved HTML code to change the path of the images to your local directory</li><li>open the page with a browser</li></ul><p>If the page does not look "right", there is something missing, like CSS, Javascript, etc. Repeat the steps for the missing parts.</p><p>As I said: You can do that with Wireshark, but it would <strong>require a lot of manual work</strong>.</p></div><div id="comment-38808-info" class="comment-info"><span class="comment-age">(30 Dec '14, 14:10)</span> Kurt Knochner ♦</div></div><span id="54939"></span><div id="comment-54939" class="comment"><div id="post-54939-score" class="comment-score"></div><div class="comment-text"><p>@Wiresharker "Now I can either reconstruct the html page without images" - How did you do that? Can you guide me a bit about how you reconstructed the HTML page?</p></div><div id="comment-54939-info" class="comment-info"><span class="comment-age">(18 Aug '16, 02:42)</span> Jesss</div></div></div><div id="comment-tools-38731" class="comment-tools"></div><div class="clear"></div><div id="comment-38731-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

