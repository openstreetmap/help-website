+++
type = "question"
title = "How to find more informations about nodes and ways?"
description = '''We&#x27;re programming an app for Windows Phone 7, and we&#x27;re using Open Street Map (OSM) as our data source. We&#x27;re using this URI: http://api.openstreetmap.org/api/0.6/map?bbox=32.0846,034.8415,32.3846,035  and we&#x27;re filling in coordinates according to the current position of the app&#x27;s user. The data we ...'''
date = "2013-08-27T14:16:00Z"
lastmod = "2013-09-07T21:19:00Z"
weight = 25853
keywords = [ "development", "information", "windowsmobile" ]
aliases = [ "/questions/25853" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to find more informations about nodes and ways?](/questions/25853/how-to-find-more-informations-about-nodes-and-ways)

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
<span id="post-25853-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25853-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-25853-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We're programming an app for Windows Phone 7, and we're using Open Street Map (OSM) as our data source.</p>
<p>We're using this URI: <a href="http://api.openstreetmap.org/api/0.6/map?bbox=32.0846,034.8415,32.3846,035">http://api.openstreetmap.org/api/0.6/map?bbox=32.0846,034.8415,32.3846,035</a> and we're filling in coordinates according to the current position of the app's user.</p>
<p>The data we receive is : "nodes", "way", and "relation".</p>
<p>this is our question:</p>
<ul>
<li>How could we get some more information about a "way", or a "node" - its name, its website, etc. ?</li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-information" rel="tag" title="see questions tagged &#39;information&#39;">information</span> <span class="post-tag tag-link-windowsmobile" rel="tag" title="see questions tagged &#39;windowsmobile&#39;">windowsmobile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Aug '13, 14:16</strong></p>
<img src="https://secure.gravatar.com/avatar/6c46c949a16eb63b46f46a16b1a61f46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yehudit&#39;s gravatar image" />
<p><span>yehudit</span><br />
<span class="score" title="61 reputation points">61</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yehudit has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Aug '13, 20:58</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0c12497903c6f3b2dd9f4d87deb127de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MagicFab&#39;s gravatar image" />
<p><span>MagicFab</span><br />
<span class="score" title="935 reputation points">935</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span></p>
</div>
</div>
<div id="comments-container-25853" class="comments-container">
&#10;</div>
<div id="comment-tools-25853" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25853-form-container" class="comment-form-container">
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

<span id="26181"></span>

<div id="answer-container-26181" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26181-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26181-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-26181-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First, unless you are writing the OSM editor, that is <a href="http://wiki.openstreetmap.org/wiki/API_usage_policy">not correct usage of 0.6 API</a> . See that page for more info on alternatives (like running your own or third party server, or switching to <a href="http://wiki.openstreetmap.org/wiki/Xapi">XAPI</a> or <a href="http://wiki.openstreetmap.org/wiki/Overpass_API">Overpass</a>. There are usage examples there, and you get your node tags too.</p>
<p>For example, sending Overpass query</p>
<pre><code>  (node(32.0846,034.8415,32.3846,035);&lt;;);out;</code></pre>
<p>returns (among other things)</p>
<pre><code>  &lt;node id=&quot;114130322&quot; lat=&quot;32.1664181&quot; lon=&quot;34.8426014&quot;/&gt;
  &lt;node id=&quot;114130323&quot; lat=&quot;32.1649314&quot; lon=&quot;34.8425907&quot;&gt;
    &lt;tag k=&quot;highway&quot; v=&quot;traffic_signals&quot;/&gt;
  &lt;/node&gt;
  &lt;node id=&quot;194227886&quot; lat=&quot;32.1274304&quot; lon=&quot;34.8489519&quot;/&gt;
  &lt;node id=&quot;195293840&quot; lat=&quot;32.3748585&quot; lon=&quot;34.9086394&quot;/&gt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Sep '13, 18:12</strong></p>
<img src="https://secure.gravatar.com/avatar/666391973130e371bf8092f70c43df28?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Matija%20Nalis&#39;s gravatar image" />
<p><span>Matija Nalis</span><br />
<span class="score" title="750 reputation points">750</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Matija Nalis has 2 accepted answers">11%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Sep '13, 17:30</strong> </span></p>
</div>
</div>
<div id="comments-container-26181" class="comments-container">
<span id="26187"></span>
<div id="comment-26187" class="comment">
<div id="post-26187-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><span>@Matija Nalis</span> From memory I think that it's the preview of XML here that's broken, not the eventual display.</p>
</div>
<div id="comment-26187-info" class="comment-info">
<span class="comment-age">(07 Sep '13, 21:19)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-26181" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26181-form-container" class="comment-form-container">
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

