+++
type = "question"
title = "Any reason not to strip symbols from wireshark/libwireshark/libwiretap?"
description = '''I usually use strip(1) on Unix/Linux systems to strip symbols from executable binaries and libraries, on the general principle that smaller executables = smaller memory footprint = better performance. As long as I&#x27;m not debugging/breakpointing the code, there shouldn&#x27;t be any need for the symbols an...'''
date = "2013-07-25T18:03:00Z"
lastmod = "2013-07-26T08:49:00Z"
weight = 23372
keywords = [ "performance", "administration", "optimize" ]
aliases = [ "/questions/23372" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Any reason not to strip symbols from wireshark/libwireshark/libwiretap?](/questions/23372/any-reason-not-to-strip-symbols-from-wiresharklibwiresharklibwiretap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23372-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23372-score" class="post-score" title="current number of votes">0</div><span id="post-23372-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I usually use strip(1) on Unix/Linux systems to strip symbols from executable binaries and libraries, on the general principle that smaller executables = smaller memory footprint = better performance. As long as I'm not debugging/breakpointing the code, there shouldn't be any need for the symbols anyway...</p><p>Doing so to the main components of Wireshark 1.10.0 makes a HUGE difference in the size of the executables:</p><ul><li>wireshark: from 10MB to 2MB</li><li>libwireshark: from 158MB to 60MB</li><li>libwiretap: from 1.5MB to 340KB</li></ul><p>I've run several tests and haven't noticed any problems - does anyone know of any reason NOT to do this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span> <span class="post-tag tag-link-administration" rel="tag" title="see questions tagged &#39;administration&#39;">administration</span> <span class="post-tag tag-link-optimize" rel="tag" title="see questions tagged &#39;optimize&#39;">optimize</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jul '13, 18:03</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p><span>wesmorgan1</span><br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span></p></div></div><div id="comments-container-23372" class="comments-container"></div><div id="comment-tools-23372" class="comment-tools"></div><div class="clear"></div><div id="comment-23372-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23374"></span>

<div id="answer-container-23374" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23374-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23374-score" class="post-score" title="current number of votes">3</div><span id="post-23374-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wesmorgan1 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I usually use strip(1) on Unix/Linux systems to strip symbols from executable binaries and libraries, on the general principle that smaller executables = smaller memory footprint = better performance.</p></blockquote><p>"Smaller executables" does <em>not</em> imply "smaller memory footprint". Not everything in an executable image ends up in the address space of the process running the executable; the code and data sections do, but the symbol table does <em>not</em> - it's in the file, but not in memory.</p><p>Stripping executable images will have only a minimal effect on performance, if it has any effect at all. The only <em>harm</em> it would cause would be if the program were to crash and, in order to try to debug the crash and get the problem fixed, the supplier of the program needed something such as a stack trace of the crash; if the symbols aren't present, the stack trace wouldn't be able to indicate what functions in the program were being called, it would only give the addresses of the functions, not their names.</p><p>Unless you have a need to save <em>disk</em> space, don't bother stripping the executables.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '13, 01:23</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-23374" class="comments-container"><span id="23387"></span><div id="comment-23387" class="comment"><div id="post-23387-score" class="comment-score"></div><div class="comment-text"><p>Weird...top(1) seems to indicate reduced memory consumption (in terms of system totals) after stripping. (I know that symbols aren't loaded by default.) I did notice a definite imporovement in launch time. Since I wasn't running it in a debugging environment, I just assumed that some internal debugging code was loading them. I'll go back and take a more detailed look, since I've obviously missed something. Thanks for the clarification.</p></div><div id="comment-23387-info" class="comment-info"><span class="comment-age">(26 Jul '13, 08:49)</span> <span class="comment-user userinfo">wesmorgan1</span></div></div></div><div id="comment-tools-23374" class="comment-tools"></div><div class="clear"></div><div id="comment-23374-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

