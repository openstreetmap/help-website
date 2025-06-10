+++
type = "question"
title = "QGIS OSMPlugin attributes"
description = '''Hi, I want to load OSM data into QGIS with the OSMPlugin. It works fine, the only problem is that all the tags are saved in one column. Is there a way to seperate each tag into one column besides the defautl ones (name, place, highway, etc.)? Thanks, Uli'''
date = "2012-11-01T09:30:00Z"
lastmod = "2012-12-05T12:55:00Z"
weight = 17350
keywords = [ "qgis", "osmplugin" ]
aliases = [ "/questions/17350" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [QGIS OSMPlugin attributes](/questions/17350/qgis-osmplugin-attributes)

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
<span id="post-17350-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17350-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17350-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I want to load OSM data into QGIS with the OSMPlugin. It works fine, the only problem is that all the tags are saved in one column. Is there a way to seperate each tag into one column besides the defautl ones (name, place, highway, etc.)?</p>
<p>Thanks,</p>
<p>Uli</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-qgis" rel="tag" title="see questions tagged &#39;qgis&#39;">qgis</span> <span class="post-tag tag-link-osmplugin" rel="tag" title="see questions tagged &#39;osmplugin&#39;">osmplugin</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Nov '12, 09:30</strong></p>
<img src="https://secure.gravatar.com/avatar/e0304055ba107b43dc134e4a9e5a955c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wasus&#39;s gravatar image" />
<p><span>Wasus</span><br />
<span class="score" title="346 reputation points">346</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wasus has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17350" class="comments-container">
&#10;</div>
<div id="comment-tools-17350" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17350-form-container" class="comment-form-container">
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

<span id="18206"></span>

<div id="answer-container-18206" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18206-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18206-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18206-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One possible solution is to save the osm file to a shapefile, open it in ArcGIS, and seperate the one column into several columns with the following python field calculator code:</p>
<pre><code>def parseAddr(textRaw, addrTag):
  #addrTag = &#39;addr:city&#39;
  text = textRaw.replace(&#39;&quot;&#39;,&#39;&#39;)
  lstTags = text.split(&#39;,&#39;)
  for i in range(0, len(lstTags)):
    lstSingleTag = lstTags[i].split(&#39;=&#39;)
    if addrTag == lstSingleTag[0]:
      tag = lstSingleTag[lstSingleTag.index(addrTag)+1]
      return tag</code></pre>
<p>Then expression for city field would be: City = parseAddr('!FieldName!', 'addr:city')</p>
<p>For streets field: Street = parseAddr('!FieldName!', 'addr:street')</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Dec '12, 12:55</strong></p>
<img src="https://secure.gravatar.com/avatar/e0304055ba107b43dc134e4a9e5a955c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wasus&#39;s gravatar image" />
<p><span>Wasus</span><br />
<span class="score" title="346 reputation points">346</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wasus has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Dec '12, 12:56</strong> </span></p>
</div>
</div>
<div id="comments-container-18206" class="comments-container">
&#10;</div>
<div id="comment-tools-18206" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18206-form-container" class="comment-form-container">
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

