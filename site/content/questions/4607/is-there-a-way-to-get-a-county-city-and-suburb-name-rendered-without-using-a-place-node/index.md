+++
type = "question"
title = "Is there a way to get a county, city and suburb name rendered without using a place=* node?"
description = '''Is there a way to map out and tag an entity such as county, city or suburb (or state, or village, etc., although I don&#x27;t work with those as a matter of practice) as a polygon and have its name rendered in the same style and at the same zoom levels as it would be rendered if it were a node tagged as ...'''
date = "2011-04-18T19:45:00Z"
lastmod = "2011-04-29T22:03:00Z"
weight = 4607
keywords = [ "rendering", "place", "mapnik" ]
aliases = [ "/questions/4607" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a way to get a county, city and suburb name rendered without using a place=\* node?](/questions/4607/is-there-a-way-to-get-a-county-city-and-suburb-name-rendered-without-using-a-place-node)

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
<span id="post-4607-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4607-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-4607-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way to map out and tag an entity such as county, city or suburb (or state, or village, etc., although I don't work with those as a matter of practice) <strong>as a polygon</strong> and have its name rendered in the same style and at the same zoom levels as it would be rendered if it were <strong>a node</strong> tagged as place=*?</p>
<p>Please note that I am <strong>not</strong> talking about the way the name of the <strong>area</strong> polygons is rendered, such as landuse=* or a building=* polygons. I am talking about the styles associated with the place=* hierarchy.</p>
<p>I am interested mostly in Mapnik, although if the answer is 'no' for Mapnik and 'yes' for another renderer, I would like to hear about that.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-place" rel="tag" title="see questions tagged &#39;place&#39;">place</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Apr '11, 19:45</strong></p>
<img src="https://secure.gravatar.com/avatar/c23c2891306229bb036de7ce63bb8c9b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ponzu&#39;s gravatar image" />
<p><span>ponzu</span><br />
<span class="score" title="2104 reputation points"><span>2.1k</span></span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ponzu has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Apr '11, 19:52</strong> </span></p>
</div>
</div>
<div id="comments-container-4607" class="comments-container">
<span id="4636"></span>
<div id="comment-4636" class="comment">
<div id="post-4636-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You might be confusing something when you say you do not want it in the way landuse or buildings behave, because actually it is the exact same way. The font and zoomlevel when the label appears depends on the style sheet. As Andy said: if you use the same styles as there already are for place nodes, the labels will look the same.</p>
</div>
<div id="comment-4636-info" class="comment-info">
<span class="comment-age">(19 Apr '11, 09:44)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
<span id="4651"></span>
<div id="comment-4651" class="comment">
<div id="post-4651-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't think I am too confused. The names of place nodes appear at earlier zooms and have different fonts for different ranks. If I were to convert a place polygon to a multipolygon, as someone suggested elsewhere, then its name would get rendered in the center, but it would be rendered according the same rules as area polygons currently do. I did not want anyone suggesting this again.</p>
<p>I understand about the stylesheets, will query Andy about them more. The question was can I tag for the existing stylesheet to get the desirable result.</p>
</div>
<div id="comment-4651-info" class="comment-info">
<span class="comment-age">(19 Apr '11, 19:55)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
</div>
<div id="comment-tools-4607" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4607-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="4632"></span>

<div id="answer-container-4632" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4632-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4632-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-4632-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, this is easy to achieve with a customised stylesheet in mapnik.</p>
<p>First, ensure the object is a candidate for the polygons table (in this case key "place" is already marked as such in the osm2pgsql default.style). Then you can add a layer definition to your mapnik style referring to the polygons table instead of the nodes table, but otherwise the same as the existing layer showing places.</p>
<p>If you use the same style rules for both the point- and polygon- layers then the text will show up in the same size and zoom levels, regardless of whether it's using the point or polygon table. And mapnik lets you use the same &lt;stylename&gt; declaration in multiple layers, so you don't need to make duplicate of the style rules.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Apr '11, 08:58</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-4632" class="comments-container">
<span id="4652"></span>
<div id="comment-4652" class="comment">
<div id="post-4652-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, I have now heard two versions of the answer: "It is easy" and "People have been bugging Mapnik about this for a long time". If it's easy, why hasn't it been implemented? Do you think anyone would mind if this became the standard behavior? We would not need place nodes anymore in addition to place polygons. The advice I received elsewhere was to delete the node once a polygon for the same entity is available. That advice either did not take labeling into consideration or did not apply to places at all (it could have been about parks and such).</p>
</div>
<div id="comment-4652-info" class="comment-info">
<span class="comment-age">(19 Apr '11, 19:58)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="4653"></span>
<div id="comment-4653" class="comment">
<div id="post-4653-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also, could you please elaborate or point me to the discussion explaining how me customizing a Mapnik stylesheet can help affect what the map looks like in <a href="http://osm.org">osm.org</a>? I am not talking about producing a custom map, but about either tweaking my tagging in case it's what's preventing the current "official" Mapnik from rendering the names, or tweaking the "official" Mapniik. I am sorry if I did not make myself clear.</p>
</div>
<div id="comment-4653-info" class="comment-info">
<span class="comment-age">(19 Apr '11, 20:02)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="4673"></span>
<div id="comment-4673" class="comment">
<div id="post-4673-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The reason it isn't being done in mapnik today is because I only recently switched place to be a polygon candidate in osm2pgsql's default.style file. Once we've had a full rendering database reload on <a href="http://osm.org">osm.org</a>, we can start showing place=* polygons as well.</p>
</div>
<div id="comment-4673-info" class="comment-info">
<span class="comment-age">(20 Apr '11, 21:35)</span> <span class="comment-user userinfo">Lennard</span>
</div>
</div>
<span id="4682"></span>
<div id="comment-4682" class="comment">
<div id="post-4682-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Excellent news. Follow-up questions: 1)Will the names be rendered in accordance with the place=* styles or same as any polygon? (Hint: I am hoping for the former). 2)Will it work on multipolygons as well as closed ways? 3)Does/will Mapnik support boundary relations? Specifically, will Mapnik respect the "label" role and generate the label where that node points, and will these relations need a place=* tag to get their labels rendered properly, or will Mapnik go on admin_level? If there are existing threads on this subject, please point me to them (Trac, forum, lists, IRC, wiki, etc.)</p>
</div>
<div id="comment-4682-info" class="comment-info">
<span class="comment-age">(20 Apr '11, 22:33)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="4713"></span>
<div id="comment-4713" class="comment">
<div id="post-4713-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>1) The plan is to have them in the same style as place=* nodes.</p>
<p>2) They're the same as far as the rendering database is concerned.</p>
<p>3) Support for this would need to come from osm2pgsql in the first place. I'm not a huge fan of the label=* role, and that's an understatement.</p>
<p>Support for place areas is distinctly different from boundary relations and admin_level. So yes, you'd need a place tag on the closed way or multipolygon relation.</p>
<p><a href="http://trac.openstreetmap.org/ticket/3110">http://trac.openstreetmap.org/ticket/3110</a> is an example from trac</p>
</div>
<div id="comment-4713-info" class="comment-info">
<span class="comment-age">(21 Apr '11, 20:52)</span> <span class="comment-user userinfo">Lennard</span>
</div>
</div>
<span id="4716"></span>
<div id="comment-4716" class="comment not_top_scorer">
<div id="post-4716-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Let's be clear that I am talking about a role=label member of a boundary/multipolgon relation, and not the type=role relation, which is a competing proposal, allegedly honored by Osmarender, which I personally have no experience using and have no interest in. The Trac ticket you linked talks about the role relation, not role member. And when you reference label=* role, this makes me think of the label key applicable, for example, on manhole covers: <a href="http://wiki.openstreetmap.org/wiki/Key:label">http://wiki.openstreetmap.org/wiki/Key:label</a></p>
</div>
<div id="comment-4716-info" class="comment-info">
<span class="comment-age">(21 Apr '11, 21:59)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="4718"></span>
<div id="comment-4718" class="comment not_top_scorer">
<div id="post-4718-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think that if Mapnik starts rendering the name of a closed way polygon and multipolygon (including boundary relation as a subclass of a multipolygon) in accordance with the style associated with the place=* tag on the (multi)polygon and in the centroid of the polygon, most people should be happy. I personally would not care much if the label role is supported or not. I thought this role was necessary to cause the label the render. But since it has nothing to do with that, I personally lost interest in it. The use cases for this role are pretty specific and rare.</p>
</div>
<div id="comment-4718-info" class="comment-info">
<span class="comment-age">(21 Apr '11, 22:05)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="4750"></span>
<div id="comment-4750" class="comment not_top_scorer">
<div id="post-4750-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When will a "full rendering database reload on <a href="http://osm.org">osm.org</a>" happen? Does that only happen irregularly, or is it going to happen automatically sometime, or is that what happens all the time? I don't understand what it means. I tried to search the wiki for an explanation, but couldn't find anything.</p>
</div>
<div id="comment-4750-info" class="comment-info">
<span class="comment-age">(23 Apr '11, 14:09)</span> <span class="comment-user userinfo">spod</span>
</div>
</div>
<span id="4751"></span>
<div id="comment-4751" class="comment not_top_scorer">
<div id="post-4751-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>To be able to render the default map on <a href="http://osm.org">osm.org</a>, we take the OSM database and process/import that into another database to suit the map renderer. This is what a "rendering database reload" means.</p>
<p>Usually, this rendering database is kept up to date by applying changes as they happen. This is the normal operating mode.</p>
<p>Every once in a while, the whole db is reloaded from scratch. This used to happen once a week when we had no minutely updates. Then once these updates matured, the full reload interval increased. The last one was done over a year ago. I'm expecting another one before the summer.</p>
</div>
<div id="comment-4751-info" class="comment-info">
<span class="comment-age">(23 Apr '11, 15:00)</span> <span class="comment-user userinfo">Lennard</span>
</div>
</div>
<span id="4757"></span>
<div id="comment-4757" class="comment not_top_scorer">
<div id="post-4757-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the info Lennard - is there a way of being informed of/finding out when the full database reload has happened, so I can check that my multipolygon labels are then being rendered correctly?</p>
</div>
<div id="comment-4757-info" class="comment-info">
<span class="comment-age">(24 Apr '11, 04:56)</span> <span class="comment-user userinfo">spod</span>
</div>
</div>
<span id="4806"></span>
<div id="comment-4806" class="comment not_top_scorer">
<div id="post-4806-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span></span><span>@Lennard</span> Let me make sure I understand. You have already made the necessary change to start having place polygon labels rendered in the style consistent with place nodes, and the reason we are not seeing them is because the database has to be fully refreshed? What about a brand new place polygon? Will it get its label rendered? My testing says it does not, but maybe I was testing prior to your change?</p>
</div>
<div id="comment-4806-info" class="comment-info">
<span class="comment-age">(25 Apr '11, 19:14)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
</div>
<div id="comment-tools-4632" class="comment-tools">
<span class="comments-showing"> showing 5 of 11 </span> <a href="#" class="show-all-comments-link">show 6 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-4632-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="4809"></span>

<div id="answer-container-4809" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4809-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4809-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-4809-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The new instructions* to handle place as polygons will only be activated once a full reimport is being done.</p>
<p>*osm2pgsql's default.style file</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Apr '11, 19:29</strong></p>
<img src="https://secure.gravatar.com/avatar/90263d23dc3f15a98d14d91e889b9d25?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lennard&#39;s gravatar image" />
<p><span>Lennard</span><br />
<span class="score" title="91 reputation points">91</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lennard has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-4809" class="comments-container">
&#10;</div>
<div id="comment-tools-4809" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4809-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="4902"></span>

<div id="answer-container-4902" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4902-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4902-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-4902-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You might want to consider creating a relation for the polygon with boundary=administrative (with the admin_level being appropriate for the type of place). You can make the place node a member of the relation. See the <a href="http://wiki.openstreetmap.org/wiki/Relation:boundary">http://wiki.openstreetmap.org/wiki/Relation:boundary</a> page for details.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Apr '11, 01:00</strong></p>
<img src="https://secure.gravatar.com/avatar/f075add936ab95d2d368f2e48f5ddc22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ebenezer&#39;s gravatar image" />
<p><span>Ebenezer</span><br />
<span class="score" title="948 reputation points">948</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ebenezer has 2 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-4902" class="comments-container">
<span id="4909"></span>
<div id="comment-4909" class="comment">
<div id="post-4909-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That doesn't do anything. The name of the place will be rendered in the place-appropriate style, but it will be due to the existence of the place node, not it's inclusion in the relation. I confirm that the name of a relation-based polygon (I.e., multipolygon or boundary) does get rendered currently in the centroid, but its style does not follow the place=* styles.</p>
</div>
<div id="comment-4909-info" class="comment-info">
<span class="comment-age">(29 Apr '11, 22:03)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
</div>
<div id="comment-tools-4902" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4902-form-container" class="comment-form-container">
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

