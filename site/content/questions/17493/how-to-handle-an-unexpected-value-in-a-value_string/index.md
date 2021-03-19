+++
type = "question"
title = "How to handle an unexpected value in a value_string?"
description = '''Hello, I want to know how to handle an unexpected value in a value_string array. For example my array looks like the following: static const value_string example[] = {  {0, &quot;result1&quot;},  {1, &quot;result2&quot;},  {2, &quot;result3&quot;},  {0, NULL} };  If I have a value like 4, I have a STATUS_ACCESS_VIOLATION error. ...'''
date = "2013-01-07T06:25:00Z"
lastmod = "2013-01-08T03:21:00Z"
weight = 17493
keywords = [ "string", "value" ]
aliases = [ "/questions/17493" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to handle an unexpected value in a value\_string?](/questions/17493/how-to-handle-an-unexpected-value-in-a-value_string)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17493-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17493-score" class="post-score" title="current number of votes">0</div><span id="post-17493-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I want to know how to handle an unexpected value in a <code>value_string</code> array. For example my array looks like the following:</p><pre><code>static const value_string example[] = {
    {0, &quot;result1&quot;},
    {1, &quot;result2&quot;},
    {2, &quot;result3&quot;},
    {0, NULL}
};</code></pre><p>If I have a value like 4, I have a <code>STATUS_ACCESS_VIOLATION</code> error. For me the last element <code>{0, NULL}</code> should avoid this unexpected behaviour, but it seems that it doesn't. Am I totally wrong? Is there any solution to my problem?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-string" rel="tag" title="see questions tagged &#39;string&#39;">string</span> <span class="post-tag tag-link-value" rel="tag" title="see questions tagged &#39;value&#39;">value</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jan '13, 06:25</strong></p><img src="https://secure.gravatar.com/avatar/878c62d2f87284c01ed450e8df7883a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alrik&#39;s gravatar image" /><p><span>Alrik</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alrik has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Jan '13, 17:36</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-17493" class="comments-container"><span id="17498"></span><div id="comment-17498" class="comment"><div id="post-17498-score" class="comment-score"></div><div class="comment-text"><blockquote><p>For me the last instruction {0, NULL} should avoid an unexpected behaviour Yes it should, how does the code using the value string look?</p></blockquote></div><div id="comment-17498-info" class="comment-info"><span class="comment-age">(07 Jan '13, 08:06)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-17493" class="comment-tools"></div><div class="clear"></div><div id="comment-17493-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17526"></span>

<div id="answer-container-17526" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17526-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17526-score" class="post-score" title="current number of votes">1</div><span id="post-17526-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Note, in particular, that <code>match_strval(4, example)</code> will return <code>NULL</code>, and if you attempt to dereference that value your code will almost certainly crash. If you want a non-null pointer to be returned for unexpected values, use <code>val_to_str()</code>, not <code>match_strval()</code>; the third argument to <code>val_to_str()</code> is a format string that's used to generate the string value for an unexpected input value, for example <code>"Unknown result (%d)"</code> to get "Unknown result (4)" for a value of 4.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jan '13, 11:34</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-17526" class="comments-container"><span id="17552"></span><div id="comment-17552" class="comment"><div id="post-17552-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your quick answers! I use the value_string with the val_to_str() function like this: val_to_str(my_param, my_value_string, "%s")</p></div><div id="comment-17552-info" class="comment-info"><span class="comment-age">(08 Jan '13, 00:17)</span> <span class="comment-user userinfo">Alrik</span></div></div><span id="17553"></span><div id="comment-17553" class="comment"><div id="post-17553-score" class="comment-score">1</div><div class="comment-text"><p><code>val_to_str(my_param, my_value_string, "%s")</code> is not valid. The argument for the format string is a 32-bit integral value, so <code>%s</code> won't work - you have to use <code>%d</code> or <code>%u</code>, and you should probably also use some additional text, such as "Unknown result".</p></div><div id="comment-17553-info" class="comment-info"><span class="comment-age">(08 Jan '13, 00:35)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="17554"></span><div id="comment-17554" class="comment"><div id="post-17554-score" class="comment-score"></div><div class="comment-text"><p>I tried with both %u and %d and it is still not working :( Anyway, i'll try another way to avoid this error.</p><p>Edit: After another try, I changed the right %s in %d and then it works!!! TY!!</p></div><div id="comment-17554-info" class="comment-info"><span class="comment-age">(08 Jan '13, 01:01)</span> <span class="comment-user userinfo">Alrik</span></div></div><span id="17558"></span><div id="comment-17558" class="comment"><div id="post-17558-score" class="comment-score"></div><div class="comment-text"><p>If there's more than one % format item in the third argument to <code>val_to_str()</code>, that's an error - only one argument is used with that string. If you're using <code>val_to_str()</code> to generate a <em>format</em> string to be later used in <em>another</em> call, you have to escape all the other % characters by writing them as <code>%%</code>.</p></div><div id="comment-17558-info" class="comment-info"><span class="comment-age">(08 Jan '13, 03:21)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-17526" class="comment-tools"></div><div class="clear"></div><div id="comment-17526-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

