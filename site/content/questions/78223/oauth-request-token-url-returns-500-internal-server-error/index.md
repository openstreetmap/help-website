+++
type = "question"
title = "OAuth request token url returns &quot;500 Internal Server Error&quot;"
description = '''Hi I am developing an Android app to upload GPX traces to OpenStreetMaps. I have registered my app and now I am testing it. But I don&#x27;t manage to get a token. When I try it both servers (test and production) return the same error: 500 I have been googling a lot, I found this issue: https://github.co...'''
date = "2021-01-04T16:48:00Z"
lastmod = "2021-01-06T19:31:00Z"
weight = 78223
keywords = [ "request_token", "api", "error500" ]
aliases = [ "/questions/78223" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OAuth request token url returns "500 Internal Server Error"](/questions/78223/oauth-request-token-url-returns-500-internal-server-error)

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
<span id="post-78223-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78223-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78223-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I am developing an Android app to upload GPX traces to OpenStreetMaps. I have registered my app and now I am testing it. But I don't manage to get a token. When I try it both servers (test and production) return the same error: 500 I have been googling a lot, I found this issue: <a href="https://github.com/openstreetmap/openstreetmap-website/issues/2222">https://github.com/openstreetmap/openstreetmap-website/issues/2222</a> And I registered a new app, but it fails too.</p>
<p>Thank you for your help.</p>
<p>Jesus Picornell</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-request_token" rel="tag" title="see questions tagged &#39;request_token&#39;">request_token</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-error500" rel="tag" title="see questions tagged &#39;error500&#39;">error500</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jan '21, 16:48</strong></p>
<img src="https://secure.gravatar.com/avatar/d46c35bd62a4346fedacd7be1eba96cb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GlobalSpark&#39;s gravatar image" />
<p><span>GlobalSpark</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GlobalSpark has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78223" class="comments-container">
<span id="78224"></span>
<div id="comment-78224" class="comment">
<div id="post-78224-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>According to <a href="https://github.com/openstreetmap/openstreetmap-website/issues/1049#issuecomment-136450085">https://github.com/openstreetmap/openstreetmap-website/issues/1049#issuecomment-136450085</a> the problem is not an unknown client but an invalid signature.</p>
</div>
<div id="comment-78224-info" class="comment-info">
<span class="comment-age">(05 Jan '21, 06:48)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="78250"></span>
<div id="comment-78250" class="comment">
<div id="post-78250-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, I am testing Openstreetmaps OAuth using an Android app. This is the related code:</p>
<pre><code>    ...
    OkHttpClient client = new OkHttpClient();
&#10;    String url3 = &quot;https://master.apis.dev.openstreetmap.org/oauth/request_token&quot;;
&#10;    RequestBody formBody = new FormBody.Builder()
            .add(&quot;consumer_key&quot;, client_id)
            .add(&quot;consumer_secret&quot;, client_secret)
            .add(&quot;callback&quot;, &quot;https://spark71.com&quot;)
            .build(); 
    Request request = new Request.Builder()
            .url(url3)
            .post(formBody)
            .build();
&#10;    client.newCall(request)
            .enqueue(new Callback() {
                @Override
                public void onFailure(final Call call, IOException e) {
&#10;...</code></pre>
<p>Thank you</p>
<p>Jesus Picornell</p>
</div>
<div id="comment-78250-info" class="comment-info">
<span class="comment-age">(06 Jan '21, 19:31)</span> <span class="comment-user userinfo">GlobalSpark</span>
</div>
</div>
</div>
<div id="comment-tools-78223" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78223-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="78232"></span>

<div id="answer-container-78232" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78232-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78232-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78232-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You are being extremely thin with details, well actually you are giving us none.</p>
<p>Literally 100's of contributors use OAuth to authorize their apps for OpenStreetMap (note no "s") every day, so it clearly does work.</p>
<p>If you really want help, then you should at least</p>
<ul>
<li>include a pointer to your source code repository or an extract o the relevant code</li>
<li>indicate which framework/library you are using.</li>
</ul>
<p>UPDATE</p>
<p>You don't seem to be actually signing the request. While it is completely possible to do implement <a href="https://tools.ietf.org/html/rfc5849#section-3.1">https://tools.ietf.org/html/rfc5849#section-3.1</a> yourself, you are going to be far better off using a library that does this for you. For example <a href="https://github.com/mttkay/signpost">signpost</a> or any other library that supports OAuth 1.0a.</p>
<p>PS: if you choose signpost you will need <a href="https://github.com/pakerfeldt/okhttp-signpost">https://github.com/pakerfeldt/okhttp-signpost</a> for use with OkHttp.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jan '21, 20:25</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Jan '21, 09:47</strong> </span></p>
</div>
</div>
<div id="comments-container-78232" class="comments-container">
&#10;</div>
<div id="comment-tools-78232" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78232-form-container" class="comment-form-container">
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

