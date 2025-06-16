+++
type = "question"
title = "How do I view stiles on the map?"
description = '''My wife is disabled, so she finds it hard to get over some stiles; therefore it would be useful to see where stiles are and their type on the map display. For example I am planning a walk round Lyme Park, OS grid reference SJ 964 823, but I don’t see the stiles I know about on http://www.openstreetm...'''
date = "2014-09-04T10:41:00Z"
lastmod = "2014-09-06T21:37:00Z"
weight = 36588
keywords = [ "stiles", "accessibility", "render" ]
aliases = [ "/questions/36588" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I view stiles on the map?](/questions/36588/how-do-i-view-stiles-on-the-map)

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
<span id="post-36588-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36588-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-36588-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My wife is disabled, so she finds it hard to get over some stiles; therefore it would be useful to see where stiles are and their type on the map display. For example I am planning a walk round Lyme Park, OS grid reference SJ 964 823, but I don’t see the stiles I know about on <a href="http://www.openstreetmap.org">http://www.openstreetmap.org</a></p>
<p>(As well as seeing the stiles on the map, it would be great if there was a photo of each stile, as no tagging system gives enough details about broken hand rails on step stiles etc.)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-stiles" rel="tag" title="see questions tagged &#39;stiles&#39;">stiles</span> <span class="post-tag tag-link-accessibility" rel="tag" title="see questions tagged &#39;accessibility&#39;">accessibility</span> <span class="post-tag tag-link-render" rel="tag" title="see questions tagged &#39;render&#39;">render</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Sep '14, 10:41</strong></p>
<img src="https://secure.gravatar.com/avatar/7cec2faf772a105273e76fa0ba68c296?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ringi&#39;s gravatar image" />
<p><span>ringi</span><br />
<span class="score" title="151 reputation points">151</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ringi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-36588" class="comments-container">
&#10;</div>
<div id="comment-tools-36588" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36588-form-container" class="comment-form-container">
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

<span id="36596"></span>

<div id="answer-container-36596" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36596-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36596-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-36596-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are two bits to this problem - mapping stiles in the first place, and displaying stiles on a map.</p>
<p>Taking the second part first, (just in case you hadn't spotted it) there are actually five map styles available on the main web site - click the thing that looks like a stack of books at the right and it allows you to switch between different background layers. Unfortunately, none of them display stiles (although the "standard" layer does display gates and hedges/fences, so you might be able to infer something from that).</p>
<p>However, it is possible to search for map features that aren't displayed on the "standard" map. Perhaps the easiest way is via "<a href="https://wiki.openstreetmap.org/wiki/Overpass_turbo">Overpass Turbo</a>". First I did a "<a href="https://wiki.openstreetmap.org/wiki/TagInfo">taginfo</a>" search for the thing that I was looking for:</p>
<p><a href="http://taginfo.openstreetmap.org/tags/barrier=stile">http://taginfo.openstreetmap.org/tags/barrier=stile</a></p>
<p>(this method does mean that you need to <a href="https://wiki.openstreetmap.org/wiki/Beginners_Guide_1.4.1">know a little bit about OSM tags</a>, unfortunately)</p>
<p>Then I selected the "Overpass Turbo" link at the right of that page, typed "Lyme Park" into the search box, selected the correct one off the list and clicked "run". The result looks like this:</p>
<p><a href="http://overpass-turbo.eu/s/4Um">http://overpass-turbo.eu/s/4Um</a></p>
<p>You can click on any of the things that you've searched for to display more information. Unfortunately there's not a huge amount of information recorded for these stiles. If you look southeast towards Derbyshire, you'll see that rather more tends to get recorded:</p>
<p><a href="http://overpass-turbo.eu/s/4Uo">http://overpass-turbo.eu/s/4Uo</a></p>
<p>It may well be that after looking at the stiles in Lyme Park via Overpass that you say "hang on - many stiles are missing!". However, it's pretty straightforward to either edit the map to add them, or to add notes so that other people can. This "<a href="https://www.openstreetmap.org/welcome">welcome</a>" page has more information.</p>
<p>As to photographs, individual OSM mappers may take photos and store them in various places (Flickr, Geograph, etc.) but there isn't really a co-ordinated effort to incorporate them into the OSM project. Of the non-OSM services that use OSM data the nearest I've seen to what you may be looking for is probably <a href="http://www.mapillary.com/map/im/bbox/53.3208122253418/53.3579063415527/-2.07762861251831/-2.03700828552246">Mapillary</a>, but there's nothing obviously available for Lyme Park.</p>
<p>Finally, one question that you might be asking is "why don't any of the map styles on the OSM website display stiles?". The short answer is that one map style can't display everything - in the words of the famous stage direction, you can't have "everything louder than everything else". There did use to be an attempt at an "everything" map style (called "Osmarender"), but for infrastructure reasons that became no longer available, and it was mostly used as a quality assurance tool rather than as an actual map (it looked horrible). The "standard" map stile is developed <a href="https://github.com/gravitystorm/openstreetmap-carto">here</a>, and the issues are created there saying things like (to take a recent example) "can we please render the names of motorway services and rest areas". In fact, there's already a <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/846">request to display stiles</a>. That doesn't mean that it'll happen at a low zoom level though; recently the "standard" map stile has moved away from "non-urban" features towards "looking nicer" when a large city is viewed. Whether that's a good idea or not is open to debate (personally I think not, but there are good arguments on either side), but I suspect that it means that you're waiting for someone to produce a different map style to the "standard" one, targetted at the <a href="http://www.who.int/gho/urban_health/situation_trends/urban_population_growth_text/en/">46%</a> of people who don't live in cities.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Sep '14, 15:24</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Sep '14, 15:49</strong> </span></p>
</div>
</div>
<div id="comments-container-36596" class="comments-container">
<span id="36599"></span>
<div id="comment-36599" class="comment">
<div id="post-36599-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, Without stiles showing up on at least one of the standard map styles, I don’t believe the data will ever be good enough to depend on. Looking at Lyme Park, the stiles look reasonable, but if I know where they all were, I would not have asked the question. Lots of gates/gaps seem to be missing, but I think the issue is that they are only recorded when a path crosses a wall, but the paths are not well defined across the grass land.</p>
</div>
<div id="comment-36599-info" class="comment-info">
<span class="comment-age">(04 Sep '14, 16:02)</span> <span class="comment-user userinfo">ringi</span>
</div>
</div>
<span id="36600"></span>
<div id="comment-36600" class="comment">
<div id="post-36600-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It a shame that there is not a tag to record the URL of a photo of an item, it would then be so easy for an app to allow a photo to be taken and the tag added to the node.</p>
</div>
<div id="comment-36600-info" class="comment-info">
<span class="comment-age">(04 Sep '14, 16:02)</span> <span class="comment-user userinfo">ringi</span>
</div>
</div>
<span id="36603"></span>
<div id="comment-36603" class="comment">
<div id="post-36603-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The problem is that we may have 100s of photos of given items. What you want sounds very similar to what Cyclestreets do for cyclists.</p>
<p>I have recently been experimenting with displaying kissing gates (not yet stiles) based on the standard render: <a href="https://www.dropbox.com/s/q20wa0niyuncjiy/kg_eg_mhead.png?dl=0.">https://www.dropbox.com/s/q20wa0niyuncjiy/kg_eg_mhead.png?dl=0.</a></p>
</div>
<div id="comment-36603-info" class="comment-info">
<span class="comment-age">(04 Sep '14, 16:26)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="36604"></span>
<div id="comment-36604" class="comment">
<div id="post-36604-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Adding to SomeoneElse's answer. It is possible to style results from Overpass-Turbo with something called MapCSS. I dont know if it would be possible to add icons for stiles, but is certainly worth investigating (not necessarily by you).</p>
</div>
<div id="comment-36604-info" class="comment-info">
<span class="comment-age">(04 Sep '14, 16:32)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="36608"></span>
<div id="comment-36608" class="comment not_top_scorer">
<div id="post-36608-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/647/sk53">@sk53</a>, I was thinking of just letting say Flickr store the image; I don’t think 100s of photos for a single stile will become a problem, as someone will have to edit the stile’s node to add the link. Another option would be agreed way to tag images on Flickr with their openstreetmap id.</p>
</div>
<div id="comment-36608-info" class="comment-info">
<span class="comment-age">(04 Sep '14, 17:28)</span> <span class="comment-user userinfo">ringi</span>
</div>
</div>
<span id="36617"></span>
<div id="comment-36617" class="comment not_top_scorer">
<div id="post-36617-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What I didn't say in the answer above (it was already way too long!) was that the maps that you see on the osm.org website aren't the be-all and end-all - it's relatively easy, for example, to create a map for a Garmin handheld (such as an eTrex series one) that displays stiles - I do that and display a dot with the name "stile". With a bit of tinkering it might even be possible to get it to route avoing stiles.</p>
<p>Another thing that you can do is to create your own web maps like the OSM ones, but rendering other information, but I suspect that that's a bit out of scope for what you wanted.</p>
</div>
<div id="comment-36617-info" class="comment-info">
<span class="comment-age">(04 Sep '14, 20:01)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="36628"></span>
<div id="comment-36628" class="comment">
<div id="post-36628-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I have done quite a bit of mapping of field boundaries,stiles &amp; gates in the southern part of the Peak District along with adding footpaths. Stile types are tagged so in theory/practice you could look for walks where there were only squeezer stiles and gates. You do get mixed stile types. i.e. stepover through squeezer. I'd only tag the latter. If you have a garmin gps you could produce a map that has different icons for the types of stiles etc. I would be happy to look at the tagging I do to see if it could be improved when it comes to producing maps that helps with disabled access.</p>
</div>
<div id="comment-36628-info" class="comment-info">
<span class="comment-age">(05 Sep '14, 07:45)</span> <span class="comment-user userinfo">dud1</span>
</div>
</div>
<span id="36634"></span>
<div id="comment-36634" class="comment not_top_scorer">
<div id="post-36634-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/9596/ringi">@ringi</a> another alternative is wikimedia commons</p>
</div>
<div id="comment-36634-info" class="comment-info">
<span class="comment-age">(05 Sep '14, 17:29)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="36636"></span>
<div id="comment-36636" class="comment not_top_scorer">
<div id="post-36636-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/3973/dud1">@dud1</a>, A stile that that only has 1 or 2 firm level steps and a good handhold of any type is not an issue for my wife. She can even cope with a high ladder stile, provided all the steps are in good order, there is a good hand rail and the platform at the top is large enough for her to stand on while I get past her to help her down. Therefore I can’t see how anything less than photo would provide enough information, as each disabled persons requirements are different.</p>
</div>
<div id="comment-36636-info" class="comment-info">
<span class="comment-age">(05 Sep '14, 19:48)</span> <span class="comment-user userinfo">ringi</span>
</div>
</div>
<span id="36637"></span>
<div id="comment-36637" class="comment not_top_scorer">
<div id="post-36637-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/3973/dud1">@dud1</a> Subjectively the tag I am looking for is “obstacle in/on path that is a lot harder to walk over then what you would expect from the type of the path”, e.g. a path in a field that you can see on Google maps satellite is grass land would benefit from a tag where there are a few rocks that need to be walked over as they are not expected, but the same rocks on Kinder Scout are just expected. (Stile tent to be hidden under trees so can’t be seen on Google maps satellite.)</p>
</div>
<div id="comment-36637-info" class="comment-info">
<span class="comment-age">(05 Sep '14, 19:49)</span> <span class="comment-user userinfo">ringi</span>
</div>
</div>
<span id="36643"></span>
<div id="comment-36643" class="comment not_top_scorer">
<div id="post-36643-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/9596/ringi">@ringi</a> - with regard to the “obstacle in/on path that is a lot harder to walk over then what you would expect from the type of the path”, I'd be tempted to just start recording things - if nothing else fits, perhaps in a note field, perhaps a new tag that you've made up. If someone comes up with a better tagging scheme later it's relatively easy to change things then, and as long as you don't pick a tag that's used already for something else, it'll be easy to find instances of your tag later.</p>
<p>For example, back in 2008 I started tagging the things to keep motorbikes off bridleways as "horse_barrier" because I didn't know what they were called. Later on when I found out that they were actually called "horse_stile", it was easy to change them to the more accepted tag. The same happened with "outside_drinking_area" as a tag applied to pubs - it was easy to change that to the more widely used "outside_seating".</p>
</div>
<div id="comment-36643-info" class="comment-info">
<span class="comment-age">(06 Sep '14, 00:25)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="36651"></span>
<div id="comment-36651" class="comment not_top_scorer">
<div id="post-36651-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Looking at the maintenance of stiles a graduation would be usefull as well. They tend to be made and forgotten or damaged and nobody makes a remark to the operator.</p>
</div>
<div id="comment-36651-info" class="comment-info">
<span class="comment-age">(06 Sep '14, 10:55)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="36653"></span>
<div id="comment-36653" class="comment not_top_scorer">
<div id="post-36653-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>A minor experiment with MapCSS and the overpass query in <a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>'s answer. Adding : "{{style: node[barrier=stile] { icon-image: url('icons/maki/triangle-12.png'); icon-width: 12; } }}" visualised the stiles, albeit with an abstract black triangle. Now to create some stile icons.</p>
</div>
<div id="comment-36653-info" class="comment-info">
<span class="comment-age">(06 Sep '14, 21:37)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-36596" class="comment-tools">
<span class="comments-showing"> showing 5 of 13 </span> <a href="#" class="show-all-comments-link">show 8 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-36596-form-container" class="comment-form-container">
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

