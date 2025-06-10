+++
type = "question"
title = "overpass docker image &quot;LZ4_decompress_safe failed&quot; runtime error"
description = '''Hi, I have installed a docker image of the overpass api server as explained here. Instead of providing data for the whole world, I configured the image to use a osm.bz2 file containing only my area of interest. Now I have reached the point where at least one query is being answered as expected, whil...'''
date = "2017-10-27T16:27:00Z"
lastmod = "2017-10-27T16:27:00Z"
weight = 60329
keywords = [ "overpass", "api", "error" ]
aliases = [ "/questions/60329" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [overpass docker image "LZ4_decompress_safe failed" runtime error](/questions/60329/overpass-docker-image-lz4_decompress_safe-failed-runtime-error)

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
<span id="post-60329-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60329-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60329-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I have installed a docker image of the overpass api server as explained <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Installation#Via_a_Docker_image">here</a>. Instead of providing data for the whole world, I configured the image to use a osm.bz2 file containing only my area of interest. Now I have reached the point where at least one query is being answered as expected, while all other get the following response:</p>
<pre><code>{
  &quot;version&quot;: 0.6,
  &quot;generator&quot;: &quot;Overpass API&quot;,
  &quot;osm3s&quot;: {
    &quot;timestamp_osm_base&quot;: &quot;2017-10-24T07:01:02Z&quot;,
    &quot;copyright&quot;: &quot;The data included in this document is from www.openstreetmap.org. The data is made available under ODbL.&quot;
  },
  &quot;elements&quot;: [
&#10;  ],
&quot;remark&quot;: &quot;runtime error: Query failed with the exception: LZ4_decompress_safe failed&quot;
}</code></pre>
<p>any suggestion on what is going on here? Is there any fix you are aware of? Thank you in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Oct '17, 16:27</strong></p>
<img src="https://secure.gravatar.com/avatar/29319458c9af6a4e94bff300a23cf956?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="frnc&#39;s gravatar image" />
<p><span>frnc</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="frnc has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60329" class="comments-container">
&#10;</div>
<div id="comment-tools-60329" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60329-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

