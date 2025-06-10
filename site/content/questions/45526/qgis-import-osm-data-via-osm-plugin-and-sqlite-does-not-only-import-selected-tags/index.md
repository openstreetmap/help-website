+++
type = "question"
title = "[closed] QGIS import osm data via OSM-plugin and sqlite does not only import selected tags"
description = '''Hello, I have the following problem: I want to use the OSM plugin to import data from a sqlite database that contains OSM data. In the &#x27;Export OSM topolgy to spatialite&#x27; dialog I choose the database file and the polygon geometry. Then I click the &#x27;Exported tags&#x27; button. This shows me the list of tag...'''
date = "2015-09-23T16:02:00Z"
lastmod = "2015-09-23T21:21:00Z"
weight = 45526
keywords = [ "qgis", "osmplugin" ]
aliases = [ "/questions/45526" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] QGIS import osm data via OSM-plugin and sqlite does not only import selected tags](/questions/45526/qgis-import-osm-data-via-osm-plugin-and-sqlite-does-not-only-import-selected-tags)

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
<span id="post-45526-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45526-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45526-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I have the following problem: I want to use the OSM plugin to import data from a sqlite database that contains OSM data. In the 'Export OSM topolgy to spatialite' dialog I choose the database file and the polygon geometry. Then I click the 'Exported tags' button. This shows me the list of tags together with the count of features. In my case, I select admin_level, which has 267 features. Now I press ok. After the export, I would expect that only 267 features are inserted in the added layer. But when I check the feature count of the new layer it has about 52000 tags, which is pretty much every polygon. When I had a look at the attribute table the admin_level field has the value NULL for every feature.</p>
<p>So, I'm not sure what I'm missing here. Any help or advice is appreciated.</p>
<p>Torsten.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-qgis" rel="tag" title="see questions tagged &#39;qgis&#39;">qgis</span> <span class="post-tag tag-link-osmplugin" rel="tag" title="see questions tagged &#39;osmplugin&#39;">osmplugin</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Sep '15, 16:02</strong></p>
<img src="https://secure.gravatar.com/avatar/a73650db3b8223073e80be878de022cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tfonline&#39;s gravatar image" />
<p><span>tfonline</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tfonline has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>23 Sep '15, 21:22</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-45526" class="comments-container">
<span id="45527"></span>
<div id="comment-45527" class="comment">
<div id="post-45527-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Questions about QGIS are better asked at <a href="http://gis.stackexchange.com">http://gis.stackexchange.com</a>.</p>
</div>
<div id="comment-45527-info" class="comment-info">
<span class="comment-age">(23 Sep '15, 16:27)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="45537"></span>
<div id="comment-45537" class="comment">
<div id="post-45537-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks, I will repost the question there</p>
</div>
<div id="comment-45537-info" class="comment-info">
<span class="comment-age">(23 Sep '15, 21:16)</span> <span class="comment-user userinfo">tfonline</span>
</div>
</div>
<span id="45539"></span>
<div id="comment-45539" class="comment">
<div id="post-45539-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>there it is: <a href="https://gis.stackexchange.com/questions/164069/qgis-import-osm-data-via-osm-plugin-and-sqlite-does-not-only-import-selected-tag">https://gis.stackexchange.com/questions/164069/qgis-import-osm-data-via-osm-plugin-and-sqlite-does-not-only-import-selected-tag</a></p>
</div>
<div id="comment-45539-info" class="comment-info">
<span class="comment-age">(23 Sep '15, 21:21)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-45526" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45526-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "moved to SE (avoiding duplicate work)" by aseerel4c26 23 Sep '15, 21:22

</div>

</div>

</div>

