+++
type = "question"
title = "[closed] Ajax issues with nominatim?"
description = '''Whenever I try to send an ajax request to nominatim I am getting an empty http response for example a query I am trying to do is:  http://nominatim.openstreetmap.org/search?q=%D7%99%D7%A8%D7%95%D7%A9%D7%9C%D7%99%D7%9D&amp;amp;accept-language=heb&amp;amp;format=json&amp;amp;polygon=1  If I try to enter the URL t...'''
date = "2010-10-25T10:29:00Z"
lastmod = "2010-10-25T15:11:00Z"
weight = 1301
keywords = [ "ajax", "nominatim", "request", "empty", "error" ]
aliases = [ "/questions/1301" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [\[closed\] Ajax issues with nominatim?](/questions/1301/ajax-issues-with-nominatim)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1301-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1301-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-1301-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Whenever I try to send an ajax request to nominatim I am getting an empty http response for example a query I am trying to do is:</p>
<pre><code>http://nominatim.openstreetmap.org/search?q=%D7%99%D7%A8%D7%95%D7%A9%D7%9C%D7%99%D7%9D&amp;accept-language=heb&amp;format=json&amp;polygon=1</code></pre>
<p>If I try to enter the URL through the web I see the page returns a valid json but when I try to request the following method using javascript / jquery I am being sent into .ajaxError functionality.</p>
<p>The exception on firebug shows 200 OK status which is wierd.</p>
<p>I had checked the params using firebug - the post data that I am posting is the same as above - the issue comes in the response itself. I am getting an empty response from nominatim.</p>
<p>I'm also pretty sure that the code is OK - it had WORKED in the past, and just stopped working a few days ago.</p>
<p>I even rolled versions back to be sure and it is the same.</p>
<p>My ajax params are:</p>
<pre><code>$.ajax({
            type: &quot;GET&quot;,
            url: url, // shown above
            data: {},
            dataType: &quot;json&quot;,
            success: function(r){ //do something },
            error:  function(r,text,exception){ //do something }
        });</code></pre>
<p>I am really trying to find something wrong in my code and to fix it, but I just don't find anything - as I mentioned - old code which I wrote and know for certain it works doesn't work anymore - that is after going back versions using svn.</p>
<p>Does anyone knows if there is an issue with nominatim? If not I would also be glad to get some mail and maybe contact them as I just don.t success to find a support mail.</p>
<p>Also if someone knows of another way to help - I would be glad to get new ideas, as I think I had lost all mine..</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ajax" rel="tag" title="see questions tagged &#39;ajax&#39;">ajax</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span> <span class="post-tag tag-link-empty" rel="tag" title="see questions tagged &#39;empty&#39;">empty</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Oct '10, 10:29</strong></p>
<img src="https://secure.gravatar.com/avatar/8484754e008e5d9905c620b0b3dbd1bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Itay%20Eng&#39;s gravatar image" />
<p><span>Itay Eng</span><br />
<span class="score" title="8 reputation points">8</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Itay Eng has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>25 Oct '10, 15:24</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span></p>
</div>
</div>
<div id="comments-container-1301" class="comments-container">
&#10;</div>
<div id="comment-tools-1301" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1301-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Other - this issue was raised on trac and dealt with there." by TomH 25 Oct '10, 15:24

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1305"></span>

<div id="answer-container-1305" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1305-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1305-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-1305-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Itay Eng has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This questions was answered and resolved on trac:</p>
<span></span>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Oct '10, 15:11</strong></p>
<img src="https://secure.gravatar.com/avatar/bda08a105bb6a4a606d47c1b27187fac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twain&#39;s gravatar image" />
<p><span>twain</span><br />
<span class="score" title="2381 reputation points"><span>2.4k</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="twain has 15 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-1305" class="comments-container">
&#10;</div>
<div id="comment-tools-1305" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1305-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

