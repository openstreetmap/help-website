+++
type = "question"
title = "How to add ward info in osm buildings"
description = '''i have buildings data from osm and ward boundaries. i need to find which building lies in which ward and add that information in the building data. INPUT: way id=&#x27;242474181&#x27; action=&#x27;modify&#x27; timestamp=&#x27;2013-10-17T11:42:37Z&#x27; uid=&#x27;1700096&#x27; user=&#x27;GautamPratik&#x27; visible=&#x27;true&#x27; version=&#x27;1&#x27; changeset=&#x27;18401...'''
date = "2013-10-26T03:14:00Z"
lastmod = "2013-10-26T20:55:00Z"
weight = 27501
keywords = [ "building", "admin_boundary", "data" ]
aliases = [ "/questions/27501" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to add ward info in osm buildings](/questions/27501/how-to-add-ward-info-in-osm-buildings)

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
<span id="post-27501-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27501-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-27501-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>i have buildings data from osm and ward boundaries. i need to find which building lies in which ward and add that information in the building data.</p>
<p>INPUT:</p>
<pre><code>way id=&#39;242474181&#39; action=&#39;modify&#39; timestamp=&#39;2013-10-17T11:42:37Z&#39; uid=&#39;1700096&#39; user=&#39;GautamPratik&#39; visible=&#39;true&#39; version=&#39;1&#39; changeset=&#39;18401787&#39;
    nd ref=&#39;2499343546&#39; 
    nd ref=&#39;2499343543&#39; 
    nd ref=&#39;2499343539&#39; 
    nd ref=&#39;2499343541&#39; 
    tag k=&#39;building&#39; v=&#39;yes&#39; 
&lt;/way&gt;</code></pre>
<p>OUTPUT:</p>
<pre><code>way id=&#39;242474181&#39; action=&#39;modify&#39; timestamp=&#39;2013-10-17T11:42:37Z&#39; uid=&#39;1700096&#39; user=&#39;GautamPratik&#39; visible=&#39;true&#39; version=&#39;1&#39; changeset=&#39;18401787&#39;
    nd ref=&#39;2499343546&#39; 
    nd ref=&#39;2499343543&#39; 
    nd ref=&#39;2499343539&#39; 
    nd ref=&#39;2499343541&#39; 
    tag k=&#39;building&#39; v=&#39;yes&#39; 
    tag k=&#39;district&#39; v=&#39;kathmandu&#39; 
    tag k=&#39;vdc&#39; v=&#39;kathmandu metropolitan city&#39; 
    tag k=&#39;ward&#39; v=&#39;4&#39; 
  &lt;/way&gt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-admin_boundary" rel="tag" title="see questions tagged &#39;admin_boundary&#39;">admin_boundary</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Oct '13, 03:14</strong></p>
<img src="https://secure.gravatar.com/avatar/651103e616e49724bb139f1a3e0a1a39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amritkarma&#39;s gravatar image" />
<p><span>amritkarma</span><br />
<span class="score" title="684 reputation points">684</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amritkarma has one accepted answer">11%</span></p>
</div>
</div>
<div id="comments-container-27501" class="comments-container">
<span id="27513"></span>
<div id="comment-27513" class="comment">
<div id="post-27513-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Where do you want to add this information? In the main database or your local copy? And why do you want to add this information to each building instead of creating one single area for every ward and attach all shared information to this area?</p>
</div>
<div id="comment-27513-info" class="comment-info">
<span class="comment-age">(26 Oct '13, 20:55)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-27501" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27501-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

