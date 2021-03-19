+++
type = "question"
title = "how to print out http request body as text from a package capture file?"
description = '''Hi, I have a capture that I can read from tshark but I can&#x27;t find an option to print out the request body as text to console. Do you know it is possible? If so, can you provide me an example? Thanks,'''
date = "2013-07-02T01:27:00Z"
lastmod = "2013-07-02T15:18:00Z"
weight = 22551
keywords = [ "tshark" ]
aliases = [ "/questions/22551" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to print out http request body as text from a package capture file?](/questions/22551/how-to-print-out-http-request-body-as-text-from-a-package-capture-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22551-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a capture that I can read from tshark but I can't find an option to print out the request body as text to console. Do you know it is possible? If so, can you provide me an example?</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jul '13, 01:27</strong></p><img src="https://secure.gravatar.com/avatar/7656adad2ef7c5ac31f6a55fcdb1734d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="seannguyen&#39;s gravatar image" /><p>seannguyen<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="seannguyen has no accepted answers">0%</span></p></div></div><div id="comments-container-22551" class="comments-container"><span id="22552"></span><div id="comment-22552" class="comment"><div id="post-22552-score" class="comment-score"></div><div class="comment-text"><p>Do you want to print the whole request body or just the requested URL/URI?</p></div><div id="comment-22552-info" class="comment-info"><span class="comment-age">(02 Jul '13, 01:45)</span> Landi</div></div></div><div id="comment-tools-22551" class="comment-tools"></div><div class="clear"></div><div id="comment-22551-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22578"></span>

<div id="answer-container-22578" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22578-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, you can print out the HTTP protocol container's decoded text with the <code>-O http</code> option in tshark if that's what you're looking for. If just one specific field, you can do <code>-T fields -e {container}</code> to have it output a specific protocol container, such as the URI if that's what you want.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jul '13, 15:18</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-22578" class="comments-container"></div><div id="comment-tools-22578" class="comment-tools"></div><div class="clear"></div><div id="comment-22578-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

