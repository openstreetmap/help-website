+++
type = "question"
title = "Extracting data, how to handle nodes with multiple keys."
description = '''Newbie...I&#x27;ll be working with OSM person (not yet found by my developer so can&#x27;t ask yet) and then sending extracted data to our web developer to add to Mysql database. I would like it in MsAccess so I can look it over first. We need to extract data from a variety of searches, including, for ex, sch...'''
date = "2019-05-25T22:44:00Z"
lastmod = "2019-05-27T17:31:00Z"
weight = 69304
keywords = [ "keys", "multiple", "values" ]
aliases = [ "/questions/69304" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Extracting data, how to handle nodes with multiple keys.](/questions/69304/extracting-data-how-to-handle-nodes-with-multiple-keys)

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
<span id="post-69304-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69304-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69304-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Newbie...I'll be working with OSM person (not yet found by my developer so can't ask yet) and then sending extracted data to our web developer to add to Mysql database. I would like it in MsAccess so I can look it over first. We need to extract data from a variety of searches, including, for ex, schools. They often have multiple key tags "Amenity=school" AND "Building=school" so on extraction they will end up in our table, I assume, in a multi-value cell in the "Key" column/field? (Or perhaps a child table for each record? I'm no DB guy). Perhaps comma or semicolon delimited like Building;Amenity? But then what happens to the values for these two keys since only one value column...perhaps same thing, School;School (guess I picked a bad example because the value is the same word in this case.) And the order would perhaps reflect which value belongs to which key in the adjacent key cell/column? Or should a new row be created somehow for each of the keys so only one in each cell (and we could eliminate new duplicate rows for these nodes later by OSM ID column filtering.)</p>
<p>Can any of the OSM filters do this easily, or perhaps it is the conversion tools that would get it into Access table for us that could do this "one row for each key" conversion, or perhaps we can just filter the data even though there are two values right along with those with one value, some kind of "or" statement? Hope I'm explaining this ok. Thanks for any advice.</p>
<p>EDIT by the way, how would our shape files be stored in Access since multiple nodes for a given record...again is is some sort of multi value cell the nodes that comprise the way should end up in, or a child table, if that is the word?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-keys" rel="tag" title="see questions tagged &#39;keys&#39;">keys</span> <span class="post-tag tag-link-multiple" rel="tag" title="see questions tagged &#39;multiple&#39;">multiple</span> <span class="post-tag tag-link-values" rel="tag" title="see questions tagged &#39;values&#39;">values</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 May '19, 22:44</strong></p>
<img src="https://secure.gravatar.com/avatar/aa3e93cbd0a635b436a0ca3a776156ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="philip&#39;s gravatar image" />
<p><span>philip</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="philip has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 May '19, 22:55</strong> </span></p>
</div>
</div>
<div id="comments-container-69304" class="comments-container">
<span id="69306"></span>
<div id="comment-69306" class="comment">
<div id="post-69306-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Similar question over at <a href="https://www.reddit.com/r/openstreetmap/comments/bstdbr/question_re_extracting_data_and_converting_into/">https://www.reddit.com/r/openstreetmap/comments/bstdbr/question_re_extracting_data_and_converting_into/</a></p>
</div>
<div id="comment-69306-info" class="comment-info">
<span class="comment-age">(25 May '19, 23:14)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="69318"></span>
<div id="comment-69318" class="comment">
<div id="post-69318-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The amenity column and building column (and basically a column for the 7 different Keys in our searches, which would usually just be null for 6 of the 7 for a given node) is a great idea, vs key column that would result in multi value cells...I believe you are generally only allowed to use one value per key on a given node so this would solve our problem. I assume it is easy to do with the various OSM data-extraction utilities? Thanks much.</p>
</div>
<div id="comment-69318-info" class="comment-info">
<span class="comment-age">(26 May '19, 11:35)</span> <span class="comment-user userinfo">philip</span>
</div>
</div>
</div>
<div id="comment-tools-69304" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69304-form-container" class="comment-form-container">
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

<span id="69319"></span>

<div id="answer-container-69319" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69319-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69319-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-69319-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sometimes an example helps. To take the keys you mentioned, "<a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dschool">amenity=school</a>" and "<a href="https://wiki.openstreetmap.org/wiki/Tag:building%3Dschool">building=school</a>", they actually mean different things within OSM (but are both in some sense "schools").</p>
<p>An "amenity=school" describes a currently active school, and is normally drawn around the edge of the grounds.</p>
<p>A "building=school" describes a building that was built as a school. It might not be part of a school currently (maybe the building is used for offices, or something else).</p>
<p>I'd suggest using <a href="https://taginfo.openstreetmap.org/tags/amenity=school">taginfo</a> and <a href="https://overpass-turbo.eu/s/JlP">overpass turbo</a> to explore the data near you so that you can see how things are tagged. That'll give you and understanding of the data and help you explain what tags you want to look for.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 May '19, 12:29</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-69319" class="comments-container">
<span id="69320"></span>
<div id="comment-69320" class="comment">
<div id="post-69320-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes thanks. We are trying to err on the side of too many vs. missing any, so while building=school may not actually be a currently functioning school, that is better, for our use, than missing some that are functioning schools, but are not also tagged with amenity=school. I also notice in the link you provided that 10% of the amenity=school nodes also have "building=school" as an additional tag. Thought it would be higher overlap. Even more bizarre is that only approx. 60,000 of the 500,000 "building=school"have "amenity=school" as an additional tag. So either a lot of schools are defunct, or people are not tagging them consistently. Thanks again.</p>
</div>
<div id="comment-69320-info" class="comment-info">
<span class="comment-age">(26 May '19, 13:07)</span> <span class="comment-user userinfo">philip</span>
</div>
</div>
<span id="69321"></span>
<div id="comment-69321" class="comment">
<div id="post-69321-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Most schools are mapped as areas including playgrounds, staff &amp; parent parking, sports fields etc. This is useful because access rights to school grounds are often controlled for pupil safety. Therefore only a few schools, typically in inner cities are likely to have both tags.</p>
</div>
<div id="comment-69321-info" class="comment-info">
<span class="comment-age">(26 May '19, 13:28)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="69322"></span>
<div id="comment-69322" class="comment">
<div id="post-69322-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'd expect relatively little overlap between those two tags. Most "amenity=school" will be drawn around the boundary of the grounds. There will be several buildings within those grounds, and these won't be tagged "amenity=school" as well because they are not, in themselves, schools - just buildings within a school.</p>
</div>
<div id="comment-69322-info" class="comment-info">
<span class="comment-age">(26 May '19, 13:29)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="69323"></span>
<div id="comment-69323" class="comment">
<div id="post-69323-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks both. So on one hand makes sense that most nodes/ways dont have multiple tags, but on other hand means we may end up with a lot of the same schools that are separate nodes/ways as both buildings and amenities? Or perhaps the multiple buildings in school are each separate nodes or ways and in a relationship of some sort with others of same school? I'm new at this so have to contemplate. Or am I misundertanding and there is no "standard" in that both amenities and buildings can be drawn as shapes? If you wanted the most accurate results for actual operating schools, and only had one choice of key/value, which would you choose?</p>
</div>
<div id="comment-69323-info" class="comment-info">
<span class="comment-age">(26 May '19, 13:51)</span> <span class="comment-user userinfo">philip</span>
</div>
</div>
<span id="69324"></span>
<div id="comment-69324" class="comment">
<div id="post-69324-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As maxerickson said above, you need to decide what you want to count - institutions or buildings. If you want to count institutions count "amenity=school"; if you want to count buildings that were built as part of schools, count "building=school". If you count "building=school" your result will include things that were built for education but no longer used for it, and things not built for education that are now used for it.</p>
</div>
<div id="comment-69324-info" class="comment-info">
<span class="comment-age">(26 May '19, 14:04)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="69327"></span>
<div id="comment-69327" class="comment not_top_scorer">
<div id="post-69327-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks again. Yeah, I see what you mean. I searched overpass turbo for buildings=school and when you zoom in it seems most are simply separate buildings in a single school. So we will stick to amenity=school, which hopefully the majority of those "clusters of buildings" are also tagged as separately. Having 5 or 10 buildings as separate records in our database as "schools" that are really part of same school is a bigger issue than missing that % that weren't tagged as amenity=school, but only 500,000 building=school and if...guessing...5 buildings per school, that is 100,000 schools tagged that way, while a million are tagged amenity=school, so seems obvious we should stick with that (plus many of those 100,000 multi-building schools will be in the million, so probably losing way less.) Appreciate the help!</p>
</div>
<div id="comment-69327-info" class="comment-info">
<span class="comment-age">(26 May '19, 21:18)</span> <span class="comment-user userinfo">philip</span>
</div>
</div>
<span id="69334"></span>
<div id="comment-69334" class="comment not_top_scorer">
<div id="post-69334-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just FYI, the building/amenity ratio can be the other way around too. In some places multiple schools are located in a single building, and the result might be a single <code>building=school</code> containing multiple <code>amenity=school</code> nodes.</p>
</div>
<div id="comment-69334-info" class="comment-info">
<span class="comment-age">(27 May '19, 17:31)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
</div>
<div id="comment-tools-69319" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-69319-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="69305"></span>

<div id="answer-container-69305" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69305-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69305-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69305-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>On the OSM side, tagging is completely freeform, there are no columns and there are essentially no rules about what tags can be applied to which objects.</p>
<p>The questions you are asking don't really have answers, in the sense that they are choices you get to make when you do the data extraction. Do you want an amenity column, do you want a building column, etc. Some tags will be contradictory and some tags will not make sense. You probably need to deal with those scenarios.</p>
<p>You'll likely end up with a list of tags you care about and a list of tags that you discard. You can look at openstreetmap-carto.lua and openstreetmap-carto.style in <a href="https://github.com/gravitystorm/openstreetmap-carto">https://github.com/gravitystorm/openstreetmap-carto</a> for examples of how the data is interpreted for a relatively complicated use case (the default tiles served on openstreetmap.org).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 May '19, 23:11</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-69305" class="comments-container">
&#10;</div>
<div id="comment-tools-69305" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69305-form-container" class="comment-form-container">
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

