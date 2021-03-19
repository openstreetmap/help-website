+++
type = "question"
title = "extend existing dissector"
description = '''I&#x27;d like to extend an existing dissector.  Current dissector display the field as a string and I would like to parse this string into tokens. Finding the handler is easy - method find_dissector, I know the field name that needs extension.  How do I take over current handling?'''
date = "2013-11-11T00:27:00Z"
lastmod = "2013-11-12T04:42:00Z"
weight = 26833
keywords = [ "dissector" ]
aliases = [ "/questions/26833" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [extend existing dissector](/questions/26833/extend-existing-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26833-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26833-score" class="post-score" title="current number of votes">0</div><span id="post-26833-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'd like to extend an existing dissector. Current dissector display the field as a string and I would like to parse this string into tokens. Finding the handler is easy - method find_dissector, I know the field name that needs extension. How do I take over current handling?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Nov '13, 00:27</strong></p><img src="https://secure.gravatar.com/avatar/2b76fb3cf251c7fea1dda7b829a8a8ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yosefk&#39;s gravatar image" /><p><span>yosefk</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yosefk has no accepted answers">0%</span></p></div></div><div id="comments-container-26833" class="comments-container"><span id="26834"></span><div id="comment-26834" class="comment"><div id="post-26834-score" class="comment-score"></div><div class="comment-text"><p>Are you trying to do this with LUA? Supplying a patch to the dissector in C trough bugzilla would be a better idea.</p></div><div id="comment-26834-info" class="comment-info"><span class="comment-age">(11 Nov '13, 01:14)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="26837"></span><div id="comment-26837" class="comment"><div id="post-26837-score" class="comment-score"></div><div class="comment-text"><p>I'm trying to extend http.request.uri field. The way I thought of doing it is: 1) attach to http handler (find_dissector) 2) register expert method to http.request.uri that will parse uri string into tokens. One issue is how to take control of http.request.uri handling from http dissector. Another issue is to plugin this extension. the plugin description is for new protocols handling. I want to extend handling of a standard, existing. protocol.</p></div><div id="comment-26837-info" class="comment-info"><span class="comment-age">(11 Nov '13, 06:22)</span> <span class="comment-user userinfo">yosefk</span></div></div></div><div id="comment-tools-26833" class="comment-tools"></div><div class="clear"></div><div id="comment-26833-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26839"></span>

<div id="answer-container-26839" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26839-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26839-score" class="post-score" title="current number of votes">0</div><span id="post-26839-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I'm trying to extend http.request.uri field.</p></blockquote><p>You can do that</p><ul><li>by changing the code of the HTTP dissector itself. That will allow you to modify the original field as you need it.</li><li>by using a (Lua) post dissector. That will <strong>not allow</strong> you to modify the original field. Instead you can read the value of the original field and add your own (modified) field. See my answer to a similar question: <code>http://ask.wireshark.org/questions/26091/how-to-display-s1apgtp_teid-as-decimal-format</code><br />
</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Nov '13, 07:11</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-26839" class="comments-container"><span id="26881"></span><div id="comment-26881" class="comment"><div id="post-26881-score" class="comment-score"></div><div class="comment-text"><p>Following Lua solution path.</p><p>The next step is to register ProtoField dynamically.</p><p>After dividing uri into tokens, I'd like to display each token by key and value. First step is to create ProtoField for each found token (Done). The second step is to add the new ProtoField into existing Proto.fields. I couldn't find references in <a href="http://www.wireshark.org/docs/wsug_html_chunked/wsluarm.html">http://www.wireshark.org/docs/wsug_html_chunked/wsluarm.html</a> Thanks YosefK</p></div><div id="comment-26881-info" class="comment-info"><span class="comment-age">(12 Nov '13, 04:16)</span> <span class="comment-user userinfo">yosefk</span></div></div><span id="26884"></span><div id="comment-26884" class="comment"><div id="post-26884-score" class="comment-score"></div><div class="comment-text"><p>can you post your code?</p></div><div id="comment-26884-info" class="comment-info"><span class="comment-age">(12 Nov '13, 04:19)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="26890"></span><div id="comment-26890" class="comment"><div id="post-26890-score" class="comment-score"></div><div class="comment-text"><blockquote><p>The second step is to add the new ProtoField into existing Proto.fields.</p></blockquote><p>wait a moment. Can you please be more precise on that?</p><p>Do you want to add a new field directly next/beneath the original HTTP fields? If so, <strong>that does not work</strong>, as I mentioned in my answer.</p><p>See also the screenshot in the link I posted. As you can see, the new decimal format of the <code>gtp.teid</code> field <strong>was added at the end of all other fields</strong> and I believe that's the only option with a <strong>post</strong> dissector.</p><p>If you want to add your fields somewhere else (directly next to the original fields and/or replacing the original fields), you need to modify the HTTP dissector code directly.</p></div><div id="comment-26890-info" class="comment-info"><span class="comment-age">(12 Nov '13, 04:42)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-26839" class="comment-tools"></div><div class="clear"></div><div id="comment-26839-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

