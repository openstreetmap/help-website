+++
type = "question"
title = "Using a variable as a Display Filter"
description = '''I am trying pass a raw captured file through a tshark display filter to generate a newer smaller file. When I run the following script everything works fine: tshark -R &quot;tcp.port == 80&quot; -r inputfile -w outputfile when I run the following: tshark -R /path/to/script/displayfilter -r inputfile -w output...'''
date = "2011-06-24T09:18:00Z"
lastmod = "2011-06-28T08:01:00Z"
weight = 4731
keywords = [ "tshark", "scripting", "display-filter" ]
aliases = [ "/questions/4731" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Using a variable as a Display Filter](/questions/4731/using-a-variable-as-a-display-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4731-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4731-score" class="post-score" title="current number of votes">1</div><span id="post-4731-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying pass a raw captured file through a tshark display filter to generate a newer smaller file. When I run the following script everything works fine:</p><p><strong>tshark -R "tcp.port == 80" -r</strong> <em>inputfile</em> <strong>-w</strong> <em>outputfile</em></p><p>when I run the following:</p><p><strong>tshark -R <code>/path/to/script/displayfilter</code> -r</strong> <em>inputfile</em> <strong>-w</strong> <em>outputfile</em></p><p>I get the error <strong>Read filters were specified both with "-R" and with additional command-line arguments</strong></p><p>the script displayfilter is<br />
<strong>#!/bin/sh<br />
echo "tcp.port == 80"</strong></p><p>I suspect it has to do with escaping the quotes, but for the life of me I can't figure it out. Any help greatly appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-scripting" rel="tag" title="see questions tagged &#39;scripting&#39;">scripting</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jun '11, 09:18</strong></p><img src="https://secure.gravatar.com/avatar/b9c8e1b3aa0d5e771215dddf69464f46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="freeat12five&#39;s gravatar image" /><p><span>freeat12five</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="freeat12five has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-4731" class="comments-container"><span id="4735"></span><div id="comment-4735" class="comment"><div id="post-4735-score" class="comment-score"></div><div class="comment-text"><p>Do you mean</p><pre><code>tshark -R /path/to/script/displayfilter -r inputfile -w outputfile</code></pre><p>or do you mean</p><pre><code>tshark -R `/path/to/script/displayfilter` -r inputfile -w outputfile</code></pre><p>The backquotes are important - if you don't specify them, TShark will see "/path/to/script/displayfilter" as the filter string, but if you do specify them, TShark will see the output of /path/to/script/displayfilter as the filter string.</p></div><div id="comment-4735-info" class="comment-info"><span class="comment-age">(24 Jun '11, 11:23)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="4741"></span><div id="comment-4741" class="comment"><div id="post-4741-score" class="comment-score"></div><div class="comment-text"><p>I do have the back quotes in the script. Thanks for catching my omission above.</p></div><div id="comment-4741-info" class="comment-info"><span class="comment-age">(24 Jun '11, 14:37)</span> <span class="comment-user userinfo">freeat12five</span></div></div><span id="4747"></span><div id="comment-4747" class="comment"><div id="post-4747-score" class="comment-score"></div><div class="comment-text"><p>Interestingly, tshark in OS X and Ubuntu allows the backquoted string without quotes but silently continues as if no filter were entered (in contrast to the behavior described here). I'd rather have tshark throw an error to notify the user and to have consistency across platforms.</p></div><div id="comment-4747-info" class="comment-info"><span class="comment-age">(24 Jun '11, 16:51)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="4750"></span><div id="comment-4750" class="comment"><div id="post-4750-score" class="comment-score"></div><div class="comment-text"><p>On what OS, and with what shell, did you see</p><pre><code>Read filters were specified both with &quot;-R&quot; and with additional command-line arguments</code></pre><p>when you did</p><pre><code>tshark -R `/path/to/script/displayfilter` -r inputfile -w outputfile</code></pre></div><div id="comment-4750-info" class="comment-info"><span class="comment-age">(25 Jun '11, 02:28)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="4783"></span><div id="comment-4783" class="comment"><div id="post-4783-score" class="comment-score"></div><div class="comment-text"><p>I recreated the symptom in Cygwin bash.</p></div><div id="comment-4783-info" class="comment-info"><span class="comment-age">(28 Jun '11, 08:01)</span> <span class="comment-user userinfo">bstn</span></div></div></div><div id="comment-tools-4731" class="comment-tools"></div><div class="clear"></div><div id="comment-4731-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="4742"></span>

<div id="answer-container-4742" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4742-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4742-score" class="post-score" title="current number of votes">2</div><span id="post-4742-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="freeat12five has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You need to quote the output of the command substitution (double-quotes, not single-quotes, so it does the command substitution):</p><pre><code>tshark -R &quot;`/path/to/script/displayfilter`&quot; -r inputfile -w outputfile</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jun '11, 14:43</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-4742" class="comments-container"></div><div id="comment-tools-4742" class="comment-tools"></div><div class="clear"></div><div id="comment-4742-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4752"></span>

<div id="answer-container-4752" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4752-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4752-score" class="post-score" title="current number of votes">0</div><span id="post-4752-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I found the issue. In the display filter, I was passing ! through awk, which made it freak out. I escaped it using and that did the trick.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jun '11, 09:58</strong></p><img src="https://secure.gravatar.com/avatar/b9c8e1b3aa0d5e771215dddf69464f46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="freeat12five&#39;s gravatar image" /><p><span>freeat12five</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="freeat12five has no accepted answers">0%</span></p></div></div><div id="comments-container-4752" class="comments-container"></div><div id="comment-tools-4752" class="comment-tools"></div><div class="clear"></div><div id="comment-4752-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4753"></span>

<div id="answer-container-4753" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4753-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4753-score" class="post-score" title="current number of votes">0</div><span id="post-4753-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Using "" (backslash)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jun '11, 10:00</strong></p><img src="https://secure.gravatar.com/avatar/b9c8e1b3aa0d5e771215dddf69464f46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="freeat12five&#39;s gravatar image" /><p><span>freeat12five</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="freeat12five has no accepted answers">0%</span></p></div></div><div id="comments-container-4753" class="comments-container"></div><div id="comment-tools-4753" class="comment-tools"></div><div class="clear"></div><div id="comment-4753-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

