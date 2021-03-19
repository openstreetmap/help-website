+++
type = "question"
title = "Wireshark crashes when comparing display filter to a string"
description = '''Hello everyone, in the last weeks I developed my first wireshark dissector in C. On my last testings there have been no errors, except one. When I want to set a display filter e.g. (&quot;proto.type == 9&quot;) it works, but as soon as I want to type in a letter instead of number wireshark crashes. I had this...'''
date = "2014-10-12T02:09:00Z"
lastmod = "2014-10-13T10:34:00Z"
weight = 36978
keywords = [ "fields", "dissector", "crashes", "display-filter" ]
aliases = [ "/questions/36978" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark crashes when comparing display filter to a string](/questions/36978/wireshark-crashes-when-comparing-display-filter-to-a-string)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36978-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36978-score" class="post-score" title="current number of votes">0</div><span id="post-36978-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone,<br />
<br />
in the last weeks I developed my first wireshark dissector in C.<br />
On my last testings there have been no errors, except one.<br />
When I want to set a display filter e.g. ("proto.type == 9") it works,<br />
but as soon as I want to type in a letter instead of number wireshark crashes.<br />
I had this error before but I found the mistake: There where the same display names on different field types.<br />
But this time there are no duplicate field names.</p><p>Any ideas yet? I have no access to the source code right now, but I will post it tomorrow. Thank you very much.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fields" rel="tag" title="see questions tagged &#39;fields&#39;">fields</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-crashes" rel="tag" title="see questions tagged &#39;crashes&#39;">crashes</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Oct '14, 02:09</strong></p><img src="https://secure.gravatar.com/avatar/cc56ba9bd225bd68cea09a404ecc0b6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lal12&#39;s gravatar image" /><p><span>lal12</span><br />
<span class="score" title="36 reputation points">36</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lal12 has 2 accepted answers">33%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Oct '14, 02:10</strong> </span></p></div></div><div id="comments-container-36978" class="comments-container"></div><div id="comment-tools-36978" class="comment-tools"></div><div class="clear"></div><div id="comment-36978-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37001"></span>

<div id="answer-container-37001" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37001-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37001-score" class="post-score" title="current number of votes">0</div><span id="post-37001-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="lal12 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>OK I found the mistake:<br />
value_string arrays have to end with an NULL element, e.g.:<br />
</p><pre><code>static const value_string packettypenames[] = {
        { 1, &quot;Type1&quot; },
        { 2, &quot;Type2&quot; },
        { 3, &quot;Type3&quot; },
        { 0, NULL } // This has to be at the end of every array
};</code></pre>Sadly I did not find a reason to this in the dissector readme, but maybe it is used as a NULL terminated array, which is mentioned in the readme for other cases.<br />
Additionally while you can find this NULL element in every example code, it is not written explicitly in the Readme, at least I did not find it.</div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Oct '14, 01:57</strong></p><img src="https://secure.gravatar.com/avatar/cc56ba9bd225bd68cea09a404ecc0b6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lal12&#39;s gravatar image" /><p><span>lal12</span><br />
<span class="score" title="36 reputation points">36</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lal12 has 2 accepted answers">33%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Oct '14, 01:58</strong> </span></p></div></div><div id="comments-container-37001" class="comments-container"><span id="37005"></span><div id="comment-37005" class="comment"><div id="post-37005-score" class="comment-score">1</div><div class="comment-text"><p>It's generally a good example to run tools/checkAPIs.pl on your dissector code: it will find all sorts of problems including un-terminated value_strings.</p></div><div id="comment-37005-info" class="comment-info"><span class="comment-age">(13 Oct '14, 03:09)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="37006"></span><div id="comment-37006" class="comment"><div id="post-37006-score" class="comment-score">1</div><div class="comment-text"><p><span></span><span>@lal12</span>,</p><p>From README.<del>developer</del>dissector (trunk) I haven't checked other branches:</p><blockquote>-- value_string ... (the last entry in the array must have a NULL 'strptr' value, to indicate the end of the array). The 'strings' field would be set to 'VALS(valstringname)'.</blockquote><p>Also section 1.10 of README.<del>developer</del>dissector lists CheckAPIs and other scripts to check your dissector for errors.</p><p>Edit: Corrected typos</p></div><div id="comment-37006-info" class="comment-info"><span class="comment-age">(13 Oct '14, 03:38)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="37016"></span><div id="comment-37016" class="comment"><div id="post-37016-score" class="comment-score"></div><div class="comment-text"><p>OK now I found it, but in the README.dissector and not in the README.developer. There I also found the information about the check scripts.</p></div><div id="comment-37016-info" class="comment-info"><span class="comment-age">(13 Oct '14, 10:00)</span> <span class="comment-user userinfo">lal12</span></div></div><span id="37021"></span><div id="comment-37021" class="comment"><div id="post-37021-score" class="comment-score"></div><div class="comment-text"><p>Oops, typos.</p></div><div id="comment-37021-info" class="comment-info"><span class="comment-age">(13 Oct '14, 10:34)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-37001" class="comment-tools"></div><div class="clear"></div><div id="comment-37001-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

