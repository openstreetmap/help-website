+++
type = "question"
title = "Submitting a Large Set of Code"
description = '''We are considering submitting a large set of code related to a set of protocols that is currently internal but will be opened over the next few months. The submission includes an entire protocol stack. I would like to talk to someone about the best/most efficient way to get the code submitted and re...'''
date = "2015-02-03T12:32:00Z"
lastmod = "2015-02-03T13:47:00Z"
weight = 39614
keywords = [ "contributing" ]
aliases = [ "/questions/39614" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Submitting a Large Set of Code](/questions/39614/submitting-a-large-set-of-code)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39614-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We are considering submitting a large set of code related to a set of protocols that is currently internal but will be opened over the next few months. The submission includes an entire protocol stack.</p><p>I would like to talk to someone about the best/most efficient way to get the code submitted and reviewed. Who is the best contact?</p></div><div id="question-tags" class="tags-container tags">contributing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Feb '15, 12:32</strong></p><img src="https://secure.gravatar.com/avatar/6a7bcd53f128960b7e664fa5ca309008?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="beastham&#39;s gravatar image" /><p>beastham<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="beastham has no accepted answers">0%</span></p></div></div><div id="comments-container-39614" class="comments-container"></div><div id="comment-tools-39614" class="comment-tools"></div><div class="clear"></div><div id="comment-39614-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39615"></span>

<div id="answer-container-39615" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39615-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is the Developers Guide section on <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSrcContribute.html">submitting changes</a> that has lots of good advice on requirements, and the wiki page on the <a href="http://wiki.wireshark.org/Development/Workflow">current procedure</a> to submit using Gerrit.</p><p>The changes will be reviewed on Gerrit and, if required, on the developers mailing list, but that's usually for more invasive changes rather than dissector additions.</p><p>We would prefer the dissectors to be built in rather than plugins and also take note of the licensing requirements, for which see the <a href="https://www.wireshark.org/faq.html">FAQ</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Feb '15, 13:47</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-39615" class="comments-container"><span id="39618"></span><div id="comment-39618" class="comment"><div id="post-39618-score" class="comment-score">1</div><div class="comment-text"><p>It might be a good idea to have one dissector per committ, to make reviewing it managble.</p></div><div id="comment-39618-info" class="comment-info"><span class="comment-age">(03 Feb '15, 14:45)</span> Anders ♦</div></div><span id="39620"></span><div id="comment-39620" class="comment"><div id="post-39620-score" class="comment-score"></div><div class="comment-text"><p>I have read all of the guides, so I'm looking for more specifics on the best/easiest way to move forward. Anders' comment is the kind of information I am looking for. To clarify, I am talking about ~11K lines of code, currently building as 16 separate plugins. I do not want to burden the core developers too much. I'll work on a plan for starting with the base dissectors and working from there.</p></div><div id="comment-39620-info" class="comment-info"><span class="comment-age">(03 Feb '15, 16:20)</span> beastham</div></div><span id="39643"></span><div id="comment-39643" class="comment"><div id="post-39643-score" class="comment-score">1</div><div class="comment-text"><p>We try to cut back on plugins as much as possible, therefore it's good practice to convert them to build-in dissectors before sending them. If coded properly this should be a simple as moving the dissector files to <code>epan/dissectors/</code> while dropping most plugin helper files.</p></div><div id="comment-39643-info" class="comment-info"><span class="comment-age">(04 Feb '15, 09:42)</span> Jaap ♦</div></div><span id="39646"></span><div id="comment-39646" class="comment"><div id="post-39646-score" class="comment-score">1</div><div class="comment-text"><p>My 2cents:</p><p>I would suggest submitting maybe one or two "base dissectors" for review as a start before going through the effort to submit all the dissectors.</p><p>That way you can get feedback on any overall issues (API usage,etc, etc) which might require changes in some/all of the rest of the dissectors.</p></div><div id="comment-39646-info" class="comment-info"><span class="comment-age">(04 Feb '15, 10:25)</span> Bill Meier ♦♦</div></div><span id="39667"></span><div id="comment-39667" class="comment"><div id="post-39667-score" class="comment-score"></div><div class="comment-text"><p>Thanks to everyone. I will work on an initial submission and build from there. I do plan to convert from plugins before submitting.</p></div><div id="comment-39667-info" class="comment-info"><span class="comment-age">(05 Feb '15, 07:14)</span> beastham</div></div></div><div id="comment-tools-39615" class="comment-tools"></div><div class="clear"></div><div id="comment-39615-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

