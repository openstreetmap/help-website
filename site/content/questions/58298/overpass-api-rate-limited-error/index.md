+++
type = "question"
title = "Overpass API rate limited error"
description = '''I&#x27;m working on a project that downloads data from openstreetmap by querying to http://overpass-api.de/api/interpreter. Sometimes, especially with asynchronous queries, the server returns this error.  &amp;lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&amp;gt;  &amp;lt;!DOCTYPE html PUBLIC &quot;-//W3C//DTD XHTML 1.0 Strict...'''
date = "2017-08-14T10:45:00Z"
lastmod = "2020-05-26T04:29:00Z"
weight = 58298
keywords = [ "openstreetmap", "overpass", "query" ]
aliases = [ "/questions/58298" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API rate limited error](/questions/58298/overpass-api-rate-limited-error)

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
<span id="post-58298-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58298-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-58298-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm working on a project that downloads data from openstreetmap by querying to <a href="http://overpass-api.de/api/interpreter"><code>http://overpass-api.de/api/interpreter</code></a>. Sometimes, especially with asynchronous queries, the server returns this error.</p>
<pre><code>    &lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
    &lt;!DOCTYPE html PUBLIC &quot;-//W3C//DTD XHTML 1.0 Strict//EN&quot;
        &quot;http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd&quot;&gt;
    &lt;html xmlns=&quot;http://www.w3.org/1999/xhtml&quot; xml:lang=&quot;en&quot; lang=&quot;en&quot;&gt;
    &lt;head&gt;
      &lt;meta http-equiv=&quot;content-type&quot; content=&quot;text/html; charset=utf-8&quot; lang=&quot;en&quot;/&gt;
      &lt;title&gt;OSM3S Response&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt;
    &lt;p&gt;The data included in this document is from www.openstreetmap.org. The data is made available under ODbL.&lt;/p&gt;
    &lt;p&gt;&lt;strong style=&quot;color:#FF0000&quot;&gt;Error&lt;/strong&gt;: runtime error: open64: 0 Success /osm3s_v0.7.54_osm_base Dispatcher_Client::request_read_and_idx::rate_limited. Please check /api/status for the quota of your IP address.
     &lt;/p&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
<p>I do not understand what the limitations are, and especially how I can solve it. Can someone help me?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Aug '17, 10:45</strong></p>
<img src="https://secure.gravatar.com/avatar/3561366bd49459f5b003a79c5dbee78c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CillaLu&#39;s gravatar image" />
<p><span>CillaLu</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CillaLu has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-58298" class="comments-container">
&#10;</div>
<div id="comment-tools-58298" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58298-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="58301"></span>

<div id="answer-container-58301" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58301-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58301-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-58301-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You're attempting to download too much data or too quickly. The usage policies of the various Overpass API instances can be found <a href="https://wiki.openstreetmap.org/wiki/Overpass_API#Introduction">here</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Aug '17, 16:55</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-58301" class="comments-container">
<span id="58304"></span>
<div id="comment-58304" class="comment">
<div id="post-58304-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Unfortunately these usage policies seem to be pretty incomplete. For example some instances have a limit on the maximum number of parallel requests which isn't mentioned here.</p>
</div>
<div id="comment-58304-info" class="comment-info">
<span class="comment-age">(14 Aug '17, 18:42)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="58306"></span>
<div id="comment-58306" class="comment">
<div id="post-58306-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot! Is there a way to query without limits? Maybe another server?</p>
</div>
<div id="comment-58306-info" class="comment-info">
<span class="comment-age">(14 Aug '17, 20:29)</span> <span class="comment-user userinfo">CillaLu</span>
</div>
</div>
<span id="58307"></span>
<div id="comment-58307" class="comment">
<div id="post-58307-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Sorry, but you obviously don't understand something fundamental.</p>
<p>Most, if not essentially all, these servers are run by volunteers with hardware and operating costs funded out of donations or the volunteers own pockets.</p>
<p>As a consequence you should not be asking if there is a unlimited service if your usage is outside the usage limits, you should either be asking how you can help or run your own service (perferably providing free access for third parties yourself).</p>
</div>
<div id="comment-58307-info" class="comment-info">
<span class="comment-age">(14 Aug '17, 21:13)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-58301" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58301-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74998"></span>

<div id="answer-container-74998" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74998-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74998-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74998-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>يظهر لي خطاء في تحميل البيانات لماذا</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 May '20, 18:15</strong></p>
<img src="https://secure.gravatar.com/avatar/4e83efb26b6a444ac56b92c38d86194d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Khalaf86-hsaan&#39;s gravatar image" />
<p><span>Khalaf86-hsaan</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Khalaf86-hsaan has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74998" class="comments-container">
<span id="75003"></span>
<div id="comment-75003" class="comment">
<div id="post-75003-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"I'm getting a mistake in downloading data why"</p>
<p>Please post a new question and describe in detail what you did.</p>
</div>
<div id="comment-75003-info" class="comment-info">
<span class="comment-age">(26 May '20, 04:29)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-74998" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74998-form-container" class="comment-form-container">
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

