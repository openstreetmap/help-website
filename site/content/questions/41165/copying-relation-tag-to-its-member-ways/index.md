+++
type = "question"
title = "copying relation tag to its member ways"
description = '''At least MapsForge (vector rendering lib) cannot handle relations and requires tags on roads. The OSM data should be transformed as selected relations have their selected tags copied to its members, like route=hiking. I am looking for a public tool to do that. Osmosis does have a tag-transform engin...'''
date = "2015-02-20T10:59:00Z"
lastmod = "2015-02-23T09:57:00Z"
weight = 41165
keywords = [ "hiking", "mapsforge", "data_processing", "relations", "tags" ]
aliases = [ "/questions/41165" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [copying relation tag to its member ways](/questions/41165/copying-relation-tag-to-its-member-ways)

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
<span id="post-41165-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41165-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-41165-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>At least MapsForge (vector rendering lib) cannot handle relations and requires tags on roads. The OSM data should be transformed as <strong>selected relations have their selected tags copied to its members</strong>, like route=hiking.</p>
<p>I am looking for a public tool to do that. Osmosis does have a tag-transform engine which should be able to do this but does not seem to, its relation matching is not even in the testing suite of the distribution.</p>
<p>Example: copy <em>'osmc:symbol', 'name', 'network', 'symbol'</em> from every relation tagged <em>route=hiking</em> to its member ways, using command line tools and country extracts.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-hiking" rel="tag" title="see questions tagged &#39;hiking&#39;">hiking</span> <span class="post-tag tag-link-mapsforge" rel="tag" title="see questions tagged &#39;mapsforge&#39;">mapsforge</span> <span class="post-tag tag-link-data_processing" rel="tag" title="see questions tagged &#39;data_processing&#39;">data_processing</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Feb '15, 10:59</strong></p>
<img src="https://secure.gravatar.com/avatar/543f907c30de5772ec0625b82264c188?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grin&#39;s gravatar image" />
<p><span>grin</span><br />
<span class="score" title="158 reputation points">158</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-41165" class="comments-container">
<span id="41171"></span>
<div id="comment-41171" class="comment">
<div id="post-41171-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Keep in mind that ways (and other elements) can belong to multiple relations. Simply moving tags from relations to their members won't work in all cases.</p>
</div>
<div id="comment-41171-info" class="comment-info">
<span class="comment-age">(20 Feb '15, 12:15)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="41180"></span>
<div id="comment-41180" class="comment">
<div id="post-41180-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/158/scai">@scai</a> true, but that's a secondary problem since it could be handled by tag-transform. Still a good point, thanks.</p>
</div>
<div id="comment-41180-info" class="comment-info">
<span class="comment-age">(20 Feb '15, 15:09)</span> <span class="comment-user userinfo">grin</span>
</div>
</div>
<span id="41181"></span>
<div id="comment-41181" class="comment">
<div id="post-41181-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Maybe that's capability MapsForge needs to add? This is the definition of "tagging for the renderer"</p>
</div>
<div id="comment-41181-info" class="comment-info">
<span class="comment-age">(20 Feb '15, 15:16)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
<span id="41182"></span>
<div id="comment-41182" class="comment">
<div id="post-41182-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/595/neuhausr">@neuhausr</a> I don't think that anyone's suggesting doing it within OSM; it's after extracting the data and before throwing it at MapsForge that's the question.</p>
</div>
<div id="comment-41182-info" class="comment-info">
<span class="comment-age">(20 Feb '15, 15:19)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="41184"></span>
<div id="comment-41184" class="comment">
<div id="post-41184-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@someoneelse</a> misunderstood, my bad!</p>
</div>
<div id="comment-41184-info" class="comment-info">
<span class="comment-age">(20 Feb '15, 15:35)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
<span id="41265"></span>
<div id="comment-41265" class="comment not_top_scorer">
<div id="post-41265-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have created the script, I'll try to prettify and publish it soon. Right now it's processing Hungary.osm in 7 minutes on a desktop pc which is quite acceptable. I try to look around in neighbouring countries how they could be represented in some standardised fashion; feeling kind of reinventing warm water, hmm.</p>
</div>
<div id="comment-41265-info" class="comment-info">
<span class="comment-age">(23 Feb '15, 09:57)</span> <span class="comment-user userinfo">grin</span>
</div>
</div>
</div>
<div id="comment-tools-41165" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-41165-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

