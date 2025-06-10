+++
type = "question"
title = "Change color of geojson node"
description = '''Hello there,  I am new to GeoJson and just out here, figuring out the basic steps. I managed to create a single Point which has a titel, description and coordinates. So far so good. Now I want to change the color of the dot.  Please feel free to take a look at the GeoJson down below.  {  &quot;type&quot;: &quot;Fe...'''
date = "2022-11-04T21:00:00Z"
lastmod = "2022-11-09T16:34:00Z"
weight = 86085
keywords = [ "nodes", "colors", "geojson" ]
aliases = [ "/questions/86085" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Change color of geojson node](/questions/86085/change-color-of-geojson-node)

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
<span id="post-86085-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86085-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86085-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello there,</p>
<p>I am new to GeoJson and just out here, figuring out the basic steps. I managed to create a single Point which has a titel, description and coordinates. So far so good. Now I want to change the color of the dot. Please feel free to take a look at the GeoJson down below.</p>
<pre><code>   {
     &quot;type&quot;: &quot;FeatureCollection&quot;,
     &quot;features&quot;: 
     [
      {
        &quot;type&quot;: &quot;Feature&quot;,
        &quot;properties&quot;: {
          &quot;name&quot;: &quot;name&quot;,
          &quot;description&quot;: &quot;cription&quot;
      },
     &quot;geometry&quot;: 
      {
        &quot;coordinates&quot;: 
         [
          -38.07457315977632,
          40.08010404958037
         ],
        &quot;type&quot;: &quot;Point&quot;
      }
     }
    ]
  }</code></pre>
<p>I tried to find a documentation but failed on this. Also tried to add "color": "#114558" under description, but that was a missguess. Instead of fillig the correct field, it added another field to the interface.</p>
<p>I hope someone in this community can help me to change the color of that node.</p>
<p>Sincerly Deborah</p>
<p>Edit: I want to Use the GeoJson file to import data to UMap</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-colors" rel="tag" title="see questions tagged &#39;colors&#39;">colors</span> <span class="post-tag tag-link-geojson" rel="tag" title="see questions tagged &#39;geojson&#39;">geojson</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Nov '22, 21:00</strong></p>
<img src="https://secure.gravatar.com/avatar/964632819d6553e75179b94e3eab63a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sheena_Asselia&#39;s gravatar image" />
<p><span>Sheena_Asselia</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sheena_Asselia has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Nov '22, 16:35</strong> </span></p>
</div>
</div>
<div id="comments-container-86085" class="comments-container">
<span id="86086"></span>
<div id="comment-86086" class="comment">
<div id="post-86086-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You would need to tell us what website/app you are using. There is no standardized way of expressing colors in GeoJSON so it is completely application specific.</p>
</div>
<div id="comment-86086-info" class="comment-info">
<span class="comment-age">(05 Nov '22, 07:32)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="86127"></span>
<div id="comment-86127" class="comment">
<div id="post-86127-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I want to use the GeoJson as an Import Methode for UMap. I hope this is what you meant :) I'll generate the geoJson from a Java Progamm and load it up onto a server</p>
</div>
<div id="comment-86127-info" class="comment-info">
<span class="comment-age">(09 Nov '22, 16:34)</span> <span class="comment-user userinfo">Sheena_Asselia</span>
</div>
</div>
</div>
<div id="comment-tools-86085" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86085-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

