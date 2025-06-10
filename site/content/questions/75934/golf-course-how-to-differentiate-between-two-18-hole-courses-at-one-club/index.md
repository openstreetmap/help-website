+++
type = "question"
title = "Golf course: How to differentiate between two 18 hole courses at one club?"
description = '''Royal Aberdeen Golf Club, in Aberdeen, Scotland, Europe, originally known as the Society of Golfers, Aberdeen, is the sixth oldest golf club in the world. The club has two 18 hole courses, Balgownie &amp;amp; Silverburn, 36 holes in total. I have this week marked up the two courses using local knowledge...'''
date = "2020-07-29T09:56:00Z"
lastmod = "2022-09-19T19:20:00Z"
weight = 75934
keywords = [ "golf" ]
aliases = [ "/questions/75934" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Golf course: How to differentiate between two 18 hole courses at one club?](/questions/75934/golf-course-how-to-differentiate-between-two-18-hole-courses-at-one-club)

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
<span id="post-75934-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75934-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-75934-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Royal Aberdeen Golf Club, in Aberdeen, Scotland, Europe, originally known as the Society of Golfers, Aberdeen, is the sixth oldest golf club in the world.</p>
<p>The club has two 18 hole courses, Balgownie &amp; Silverburn, 36 holes in total.</p>
<p>I have this week marked up the two courses using local knowledge and JOSM with over tracing of the sattelite images in the usual way.</p>
<p>How can I mark each hole as belonging to it's distinct course?</p>
<p>At the moment the two different 18 hole courses can be seperated, becasue the Silverburn course holes have no names, where as the Balgownie course holes all have names.</p>
<p>To make the distinction can I draw a way around each course and create a relationship, which is difficult to do becasue the fairways are sometimes mixed together in some places, or is there some way to mark the tags for each distinct fairway &amp; course?</p>
<p>For example, would I do something like add an extra identifying tag to each of tee, hole, pin, fairway etc?</p>
<p>Here is the osm.fr rendering, which I think is clearer and therefore better than the osm.org rendering. <a href="http://tile.openstreetmap.fr/?zoom=16&amp;lat=57.18025&amp;lon=-2.07854&amp;layers=B00000000">http://tile.openstreetmap.fr/?zoom=16&amp;lat=57.18025&amp;lon=-2.07854&amp;layers=B00000000</a></p>
<p>Ideally this needs to be at the point where an overpass query can produce something useful e.g:</p>
<p><strong>club course hole name distance par handicap</strong></p>
<p>"royal aberdeen" silverburn 1 - etc etc etc<br />
"royal aberdeen" silverburn 2 - etc etc etc<br />
.<br />
..<br />
...</p>
<p>"royal aberdeen" balownie 1 First etc etc etc<br />
"royal aberdeen" balownie 2 Pool etc etc etc<br />
.<br />
..<br />
...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-golf" rel="tag" title="see questions tagged &#39;golf&#39;">golf</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Jul '20, 09:56</strong></p>
<img src="https://secure.gravatar.com/avatar/5aa3b27b889fb0752ee8c2d2bff38c49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ABZ_OSM&#39;s gravatar image" />
<p><span>ABZ_OSM</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ABZ_OSM has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Jul '20, 10:11</strong> </span></p>
</div>
</div>
<div id="comments-container-75934" class="comments-container">
&#10;</div>
<div id="comment-tools-75934" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75934-form-container" class="comment-form-container">
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

<span id="75935"></span>

<div id="answer-container-75935" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75935-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75935-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-75935-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hard as it may sound, you have to take a step back from thinking about how it <em>looks</em> on the map, and instead think about what makes sense from a data modelling perspective.</p>
<p>I am not into golf but the way you say it, fairways and holes belong to one course but a fairway can occasionally belong to two courses? In that case, it would make sense to create a relation for each course - perhaps a "site" type relation, certainly not a multipolygon! - with all the holes, fairways and stuff as members. That way, the same fairway <em>can</em> belong to two different courses.</p>
<p>If, on the other hand, a fairway and a hole can only ever belong to one course, then you could also invent a tag - perhaps some form of the <code>ref</code> tag, like <code>course_ref</code>, and apply that to each of the objects.</p>
<p>Neither of these techniques will lead to different rendering results on the standard maps. But a hyothetical "interactive golf map" could, with the help of a data service like Overpass, do things like "display all features that are part of the XYZ course" - something that your initial idea of "drawing a way around it" would not allow.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jul '20, 10:07</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span> </br></br></p>
</div>
</div>
<div id="comments-container-75935" class="comments-container">
<span id="75936"></span>
<div id="comment-75936" class="comment">
<div id="post-75936-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Frederik,</p>
<p>Thanks you for your thoughtful helpful reply.</p>
<p><strong>&gt; "Hard as it may sound, you have to take a step back from thinking about how it looks on the map, and instead think about what makes sense from a data modelling perspective."</strong></p>
<p>Yes that's very important otherwise we won't be able to write complex useful queries in overpass. I am not a software coder or developer. The holes in my conceptual knowledge are frustrating, particularly regards how to create meaningful relationships, as you describe, and the finer detail and not so finer detail of constructing what I feel should be fairly easy and intuitive overpass queries.</p>
</div>
<div id="comment-75936-info" class="comment-info">
<span class="comment-age">(29 Jul '20, 10:48)</span> <span class="comment-user userinfo">ABZ_OSM</span>
</div>
</div>
<span id="75937"></span>
<div id="comment-75937" class="comment">
<div id="post-75937-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><strong>&gt; "I am not into golf but the way you say it, fairways and holes belong to one course but a fairway can occasionally belong to two courses?"</strong></p>
<p>I'm not into golf either. I see these big green spaces locally and they are empty so I thought to fill some of them up. Golf is not an exclusive game here in Scotland, Europe, as it often is elsewhere. So we have many courses. I've filled up three and improved some others.</p>
<p>Yes and sometimes, within the same course, fairways and a green can belong to two different holes, for example, holes 9 and 13 on the Silverburn course share the same green.</p>
</div>
<div id="comment-75937-info" class="comment-info">
<span class="comment-age">(29 Jul '20, 10:49)</span> <span class="comment-user userinfo">ABZ_OSM</span>
</div>
</div>
<span id="75938"></span>
<div id="comment-75938" class="comment">
<div id="post-75938-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><strong>&gt; "In that case, it would make sense to create a relation for each course - perhaps a "site" type relation, certainly not a multipolygon!</strong></p>
<p>Such relationships and multipolygon's is an area of OSM that I still do not understand, which is frustrating.<br />
I am guessing that the hardest situation for many people is when they see a multi polygon with holes in it when editing ambient features of interest. Scary! In JOSM I just avoid these when I see them.<br />
When I see pop-up's like multi polygon "inner" and "outer" I just abandon and avoid changes.</p>
<p>One thing I am sure of, though, is that this these are not difficult to understand.</p>
<p>I just can't find a resource that makes it simple to see through. I haven't really persued this udnerstanding though.</p>
<p>The same for creating meaningful relationships between objects as you suggest as a possible solution.</p>
<p>If you have any useful learning resource pointers these would be appreciated. I've just discovered this forum so will have a look on here too.</p>
</div>
<div id="comment-75938-info" class="comment-info">
<span class="comment-age">(29 Jul '20, 10:49)</span> <span class="comment-user userinfo">ABZ_OSM</span>
</div>
</div>
<span id="75939"></span>
<div id="comment-75939" class="comment">
<div id="post-75939-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><strong>&gt; "If, on the other hand, a fairway and a hole can only ever belong to one course, then you could also invent a tag - perhaps some form of the ref tag, like course_ref, and apply that to each of the objects".</strong></p>
<p>I was thinking that might be the way to go, where there is no mixed identity of each hole/ fairway / green etc.</p>
</div>
<div id="comment-75939-info" class="comment-info">
<span class="comment-age">(29 Jul '20, 10:49)</span> <span class="comment-user userinfo">ABZ_OSM</span>
</div>
</div>
<span id="75940"></span>
<div id="comment-75940" class="comment">
<div id="post-75940-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>My original post has been edited, possibly since you first read it, to contain reference to overpass. The reason I initially considered this problem of naming each of the 18 hole courses with in this one golf club, was becasue of overpass and, as things are just now, inability to make a distinction between the holes belonging to each course.</p>
</div>
<div id="comment-75940-info" class="comment-info">
<span class="comment-age">(29 Jul '20, 10:56)</span> <span class="comment-user userinfo">ABZ_OSM</span>
</div>
</div>
<span id="75944"></span>
<div id="comment-75944" class="comment not_top_scorer">
<div id="post-75944-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Relations can be easy to break if you're not careful, but are relatively simple in concept. 'Structurally' they are lists of other elements in a specific order with the option to label each element with a <em>role</em> to identify what that element does. They are the only type of element with a compulsory tag: the <code>type=*</code> tag is used to indicate what the roles in a particular relation mean and to hint at what other tags to expect. As new relation types can start as variations of old ones this can sometimes be confusing, but makes them very flexible.</p>
<p>Multipolygons are described quite well <a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon">on the wiki</a> and are generally quite well supported by software, but can sometimes require a bit of housekeeping to keep their loops intact and free of self intersections.</p>
</div>
<div id="comment-75944-info" class="comment-info">
<span class="comment-age">(29 Jul '20, 17:08)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="75955"></span>
<div id="comment-75955" class="comment not_top_scorer">
<div id="post-75955-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks <a href="https://help.openstreetmap.org/users/4426/insertuser"></a><a href="https://help.openstreetmap.org/users/4426/insertuser">@InsertUser</a>. Your comments are useful to me.<br />
After a thorough look at <a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon">https://wiki.openstreetmap.org/wiki/Relation:multipolygon</a> I find nothing there that is not straightforward and simple.<br />
Everything on that page is simple &amp; makes perfect sense.</p>
<p>I also downloaded the JOSM plugin <a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins/Relation_Toolbox">https://wiki.openstreetmap.org/wiki/JOSM/Plugins/Relation_Toolbox</a> and had a good look through it while following this explanatory video <a href="https://www.youtube.com/watch?v=jfKfjxK7dYk">https://www.youtube.com/watch?v=jfKfjxK7dYk</a></p>
<p>which was helpful. I'm still not sure when it is appropriate to create relationships though.</p>
<p>I think I need a more in depth resource that explains the necessity for these with many examples.</p>
<p>I will keep looking at the various resources though, I'm sure I will get it after a while.</p>
</div>
<div id="comment-75955-info" class="comment-info">
<span class="comment-age">(30 Jul '20, 11:11)</span> <span class="comment-user userinfo">ABZ_OSM</span>
</div>
</div>
<span id="85660"></span>
<div id="comment-85660" class="comment not_top_scorer">
<div id="post-85660-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It is possible that there is a shared green and fairway. I just came across this for the first time this past weekend. You can see it here: <a href="https://www.openstreetmap.org/#map=18/47.53602/-122.14515">https://www.openstreetmap.org/#map=18/47.53602/-122.14515</a> This also has connecting fairways as well. In this one case both holes belong to the same course, but this golf club actually has two courses. With this in mind I would not be surprised if there is a golf club out there where the two courses have a shared green/fairway.</p>
</div>
<div id="comment-85660-info" class="comment-info">
<span class="comment-age">(19 Sep '22, 19:20)</span> <span class="comment-user userinfo">rbrundritt</span>
</div>
</div>
</div>
<div id="comment-tools-75935" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-75935-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75980"></span>

<div id="answer-container-75980" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75980-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75980-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-75980-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is a follow-up to Frederik's suggestions.</p>
<p>I would prefer the site relation to map this. If you want to use a tag, that should be fine as well. Is easier to handle for occasional users, but makes handling data a bit more complicated - you don't have a single object (the relation) but have to search for a specific key and hope that there is no other course with the same name elsewhere.</p>
<p>The tag 'ref_course' is not really a common choice:</p>
<ul>
<li>Tags like "ref_XYZ" are not used much, so it should rather be "ref:XYZ".</li>
<li>I wouldn't call the name of the course a 'ref' either, it's still a name.</li>
</ul>
<p>My idea would be 'golf:course:name' or something similar. There are already a few 'golf:course:XZ' tags used for details of the course itself, so it might be reasonable to use this scheme on parts of the course as well.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Aug '20, 19:17</strong></p>
<img src="https://secure.gravatar.com/avatar/9fbbc400eb10c1432ab84779b6f7e539?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mueschel&#39;s gravatar image" />
<p><span>mueschel</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mueschel has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-75980" class="comments-container">
<span id="75984"></span>
<div id="comment-75984" class="comment">
<div id="post-75984-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks <a href="https://help.openstreetmap.org/users/14343/mueschel"></a><a href="https://help.openstreetmap.org/users/14343/mueschel">@Mueschel</a>,</p>
<p>I have changed the tags from <em>ref_course</em> to <em>golf:course:name</em>.</p>
<p>This query <a href="http://overpass-turbo.eu/s/WFr">http://overpass-turbo.eu/s/WFr</a> does limit it's search area to within the specific golf club, which is what a query should do if there is more than one Silverburn or Balgownie Links course across the world which there may be, as you say.</p>
<p>I do not fully understand the process of creating relationships within JOSM. My concern with creating realtionships is that I could create a mess which would be alot of work for me or someone else to undo.</p>
<p>Perhaps relationships are as intuitive and easy as they seem. Certianly it is easy to understand how outer polygons can have inner polygons etc. The concept is easy to understand. But something about it just does not click with me and I have yet to find a good intuitive video or explanatory page with lots of practical worked examples. I did try creating realtionships on the golf course using the <a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins/Relation_Toolbox">https://wiki.openstreetmap.org/wiki/JOSM/Plugins/Relation_Toolbox</a> plugin for JOSM. It still feel I'm creating a tangled mess, so I undid it. It feels like ERD's vs practical implementation in DBRM systems if you see what I mean. I'm not a database person.</p>
</div>
<div id="comment-75984-info" class="comment-info">
<span class="comment-age">(02 Aug '20, 10:53)</span> <span class="comment-user userinfo">ABZ_OSM</span>
</div>
</div>
<span id="75985"></span>
<div id="comment-75985" class="comment">
<div id="post-75985-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For example here is a video of someone adding a speed camera as a relationship, I think, to a road, in JOSM.</p>
<p>I'm sure he knows what he's doing, but it just looks like jibberish to me.</p>
<p><a href="https://www.youtube.com/watch?v=2tnohs_8gFY">https://www.youtube.com/watch?v=2tnohs_8gFY</a></p>
</div>
<div id="comment-75985-info" class="comment-info">
<span class="comment-age">(02 Aug '20, 11:05)</span> <span class="comment-user userinfo">ABZ_OSM</span>
</div>
</div>
<span id="75986"></span>
<div id="comment-75986" class="comment">
<div id="post-75986-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Don't worry - as long you add just a relation in your changeset, there is not much that can go wrong.</p>
<ul>
<li><p>Go to the relation window (Alt-Shift-R), click on the plus sign to make a new relation.</p></li>
<li><p>Add your tags in the top table, including type=site</p></li>
<li><p>Select some of the objects you want to add.</p></li>
<li><p>In the edit-relation window click on the left-facing arrows to add the selection to the relation.</p></li>
<li><p>Order of entries doesn't matter in your case, and you don't need to add any roles to the objects.</p></li>
<li><p>Repeating adding objects and tags until done.</p></li>
</ul>
</div>
<div id="comment-75986-info" class="comment-info">
<span class="comment-age">(02 Aug '20, 11:07)</span> <span class="comment-user userinfo">mueschel</span>
</div>
</div>
</div>
<div id="comment-tools-75980" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75980-form-container" class="comment-form-container">
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

