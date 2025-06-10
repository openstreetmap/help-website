+++
type = "question"
title = "place, boundary tags reorganization for an entire country"
description = '''Motivation &amp;amp; Background (I will try to explain everything leading up to the question, so if you don&#x27;t want to read that, go straight to the last section.) I noticed that Nominatim search results for South Korea was in a complete mess. So I&#x27;m in the process of doing a complete overhaul of the bou...'''
date = "2012-09-12T04:19:00Z"
lastmod = "2012-09-12T16:24:00Z"
weight = 15984
keywords = [ "node", "boundary", "nominatim", "place", "area" ]
aliases = [ "/questions/15984" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [place, boundary tags reorganization for an entire country](/questions/15984/place-boundary-tags-reorganization-for-an-entire-country)

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
<span id="post-15984-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15984-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-15984-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><strong>Motivation &amp; Background</strong></p>
<p><em>(I will try to explain everything leading up to the question, so if you don't want to read that, go straight to the last section.)</em></p>
<p>I noticed that Nominatim search results for South Korea was in a complete mess. So I'm in the process of doing a complete overhaul of the boundaries in the hopes of having a coherent and consistent structure.</p>
<p><strong>Notes</strong></p>
<p>The boundaries for the provinces and cities in this country is well-defined, and they can be directly correlated to place=* since major settlements all fall within city borders. So it's only a matter of putting up the boundaries and tagging appropriately, as far as the scope of my work is concerned.</p>
<p><strong>Progress</strong></p>
<p>I was able to create an entire administrative boundary for the country (admin_level=2; the old one was mostly redacted by the bot, but it was inaccurate anyway), as well as for all the provinces / metropolitan cities (admin_level=4).</p>
<p>Most recently, I placed the admin boundaries for all the cities / counties (admin_level=6) within the most populous province, Gyeonggi-do, with plans to expand this effort to other provinces. You can see that the country will have some relatively fine-grained administrative boundaries placed soon.</p>
<p><strong>Problem!</strong></p>
<p>I was initially making boundary relations that was tagged with boundary=administrative and admin_level=*. There were nodes tagged with place=* near the city centres, so I left them at that - they also seem to be where the map renderer puts the label. This apparently "used to be" how it should be done.</p>
<p>But then I noticed that Nominatim began to recognize both the boundary relation and the node, resulting in two search results, not one. The node result comes out as (city name), (city name), (province), (country) - the first one being the node, and the second one being the boundary relation. So this clearly wasn't what I wanted to achieve.</p>
<p>Upon further reading of this subject in the Help, Wiki, and other places, it seems that the "current" way to go about it is... when a boundary relation defining the area is created, move the place tag into it, and delete the node that originally had the tag. You don't want to duplicate data on two places in OSM, so I thought that sounded logical.</p>
<p>So I removed all the nodes containing the place=* tag for the provinces and added it to their boundary relations. This did solve the Nominatim search problem. When it was time to do the same for the cities, I noticed another issue - I would like to have the label near the city center, not somewhere in the middle of the defined area. You can define a node as 'label' in the boundary relation to do this, apparently.</p>
<p>However, there are lots of either outdated or conflicting info on whether a label would properly render at all. Some place says that 'label' node won't yet work, and you need a separate node with place=* tag in order for the place label to be rendered.</p>
<p><strong>So the Questions are...</strong></p>
<ol>
<li><p>Will the current OSM renderer put the province / city / etc. name on the center of the (administrative) boundary relations if it has a place=* defined? I know that a node with place=* will have its name rendered, so I want to know if this is true <strong>now</strong> for boundary relations, too.</p></li>
<li><p>If so, will having a 'label' node in that relation let me position the label? Some old post mentioned this not being the case, so I'm hesitant.</p></li>
<li><p>With the completion of national boundary relation (admin_level=2), it would only make sense that even the place=country tag should be added to the relation and have the separate node deleted, for the sake of consistency. Currently, the Wiki says that place=country should only be put in a node, but place=continent and place=state can be put in an area, so that doesn't sound consistent. Should I keep the node or not? This one is related to the previous questions, since I don't want the country label to go missing.</p></li>
</ol>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-place" rel="tag" title="see questions tagged &#39;place&#39;">place</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Sep '12, 04:19</strong></p>
<img src="https://secure.gravatar.com/avatar/580f3c1e083a5ec1bedd3f0472e50f42?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="namuori&#39;s gravatar image" />
<p><span>namuori</span><br />
<span class="score" title="106 reputation points">106</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="namuori has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-15984" class="comments-container">
&#10;</div>
<div id="comment-tools-15984" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15984-form-container" class="comment-form-container">
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

<span id="16000"></span>

<div id="answer-container-16000" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16000-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16000-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-16000-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="namuori has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ol>
<li><p>OSM tiles do not currently render labels for relations</p></li>
<li><p>No, this was the proposal but I don't believe it is implemented</p></li>
<li><p>The country place node is far less useful that other nodes, but I would say for consistency should be included.</p></li>
</ol>
<p>Its worth noting that Nominatim was recently (in the last 2 weeks) upgraded to handle duplicate node+relations pairs and to follow and merge data based on the label relation member. Given this my current recommendation would be:</p>
<ol>
<li>Create a node tagged place=* with suitable name/tags at the central location of the admin feature (this may not be the geometric center, but rather the place that would subjectively by thought of as the center)</li>
<li>Create an administrative boundary relation with admin_level defining the boundary of the feature in the normal way</li>
<li>Add a 'label' member to that relation linking the label node and the relation (nominatim and other data users can use this to deduplicate data)</li>
<li>Add a wikipedia tag to either the node or relation to allow Nominatim to work out the importance of the feature</li>
</ol>
<p>This would be my current gold standard for admin data to best work with both Nominatim and tile rendering while avoiding 'tagging for the renderer'.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Sep '12, 13:21</strong></p>
<img src="https://secure.gravatar.com/avatar/bda08a105bb6a4a606d47c1b27187fac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twain&#39;s gravatar image" />
<p><span>twain</span><br />
<span class="score" title="2381 reputation points"><span>2.4k</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="twain has 15 accepted answers">40%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Sep '12, 14:19</strong> </span></p>
</div>
</div>
<div id="comments-container-16000" class="comments-container">
<span id="16003"></span>
<div id="comment-16003" class="comment">
<div id="post-16003-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>To avoid duplicates in Nominatim, your forgot to mention the new feature with the role "admin_centre" in the boundary relation linked to the "place" node (the one which is the administrative centre e.g. the capital for a country or a town or city for a region, province, county or municipality).</p>
</div>
<div id="comment-16003-info" class="comment-info">
<span class="comment-age">(12 Sep '12, 14:08)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="16005"></span>
<div id="comment-16005" class="comment">
<div id="post-16005-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No, for things that are exactly the same you should use the 'label' relation member. admin_centre is for things like 'Sheffield (node)' is the admin_centre of 'South Yorkshire (relation)'. label is for things like 'Sheffield (node)' is the label for the 'Sheffield (relation)'</p>
</div>
<div id="comment-16005-info" class="comment-info">
<span class="comment-age">(12 Sep '12, 14:12)</span> <span class="comment-user userinfo">twain</span>
</div>
</div>
<span id="16010"></span>
<div id="comment-16010" class="comment">
<div id="post-16010-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I didn't speak about label issue but Nominatim search results duplicates as mentionned in the question. admin_centre has to point to the related administrative place, nothing to do if it is 'exactly the same' or not. If you understand it like this, then I failed to document it on the wiki (yes I created this role a long time ago).</p>
</div>
<div id="comment-16010-info" class="comment-info">
<span class="comment-age">(12 Sep '12, 15:47)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="16015"></span>
<div id="comment-16015" class="comment">
<div id="post-16015-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>yes, my understanding is that admin_centre points to a a related feature (which may or may not have the same name, but is definitely not the exact same place). The question asks about duplicated data i.e. where we have both a place=* node and a boundary=administrative relation for exactly the same place and how to avoid/handle this duplication. In context admin_centre is not relevant although it may be additional useful information to add to a relation.</p>
</div>
<div id="comment-16015-info" class="comment-info">
<span class="comment-age">(12 Sep '12, 16:24)</span> <span class="comment-user userinfo">twain</span>
</div>
</div>
</div>
<div id="comment-tools-16000" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16000-form-container" class="comment-form-container">
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

