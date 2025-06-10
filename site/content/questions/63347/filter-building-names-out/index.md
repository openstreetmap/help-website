+++
type = "question"
title = "Filter building names out"
description = '''Let&#x27;s try again.  osmfilter mi.o5m --drop-tags=&quot;amenity= name=&quot; --drop-tags=&quot;tourism= name=&quot; --drop-tags=&quot;leisure= name=&quot; --drop-tags=&quot;shop= name=&quot; --drop-tags=&quot;office= name=&quot; --drop-tags=&quot;craft= name=&quot; --drop-tags=&quot;club= name=&quot; --drop-tags=&quot;government= name=&quot; --drop-tags=&quot;building= name=&quot; --drop-ta...'''
date = "2018-05-06T16:39:00Z"
lastmod = "2018-05-14T16:18:00Z"
weight = 63347
keywords = [ "boundaries", "ways", "osmfilter", "polygons", "polygon" ]
aliases = [ "/questions/63347" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Filter building names out](/questions/63347/filter-building-names-out)

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
<span id="post-63347-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63347-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-63347-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Let's try again.</p>
<p>osmfilter mi.o5m <strong>--drop-tags="amenity= name=" --drop-tags="tourism= name=" --drop-tags="leisure= name=" --drop-tags="shop= name=" --drop-tags="office= name=" --drop-tags="craft= name=" --drop-tags="club= name=" --drop-tags="government= name=" --drop-tags="building= name=" --drop-tags="man_made= name=" --drop-tags="landuse= name="</strong> --drop-author -o=mi.osm</p>
<p>That seems to be removing what we want. However it's also removing building boundaries or ways or whatever you call them. So cities now only have roads and highways and such. What's the command to keep all boundaries? --keep-ways? how exactly?</p>
<p>Clarification. We want building polygons to stay and get rid of names. Boundaries is the wrong word for that.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span> <span class="post-tag tag-link-polygons" rel="tag" title="see questions tagged &#39;polygons&#39;">polygons</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 May '18, 16:39</strong></p>
<img src="https://secure.gravatar.com/avatar/7dc2ca85ad0fdecfb5c66a390b83180a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gfitz&#39;s gravatar image" />
<p><span>gfitz</span><br />
<span class="score" title="46 reputation points">46</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gfitz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 May '18, 23:32</strong> </span></p>
</div>
</div>
<div id="comments-container-63347" class="comments-container">
<span id="63384"></span>
<div id="comment-63384" class="comment">
<div id="post-63384-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>surely you just want --drop-tags="name="</p>
</div>
<div id="comment-63384-info" class="comment-info">
<span class="comment-age">(08 May '18, 14:21)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="63385"></span>
<div id="comment-63385" class="comment">
<div id="post-63385-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Will that remove roads names?</p>
</div>
<div id="comment-63385-info" class="comment-info">
<span class="comment-age">(08 May '18, 15:13)</span> <span class="comment-user userinfo">gfitz</span>
</div>
</div>
<span id="63398"></span>
<div id="comment-63398" class="comment not_top_scorer">
<div id="post-63398-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, it would remove all names.</p>
</div>
<div id="comment-63398-info" class="comment-info">
<span class="comment-age">(09 May '18, 17:50)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="63399"></span>
<div id="comment-63399" class="comment not_top_scorer">
<div id="post-63399-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>My question clearly asked about removing name tags from buildings only and amenity tourism etcetera. Already trying something else.</p>
</div>
<div id="comment-63399-info" class="comment-info">
<span class="comment-age">(09 May '18, 17:58)</span> <span class="comment-user userinfo">gfitz</span>
</div>
</div>
<span id="63400"></span>
<div id="comment-63400" class="comment">
<div id="post-63400-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You didn't say that you wanted to keep names for roads, though.</p>
</div>
<div id="comment-63400-info" class="comment-info">
<span class="comment-age">(09 May '18, 18:40)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="63408"></span>
<div id="comment-63408" class="comment not_top_scorer">
<div id="post-63408-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>--drop-tags="amenity=name tourism=name leisure=name shop=name office=name craft=name club=name government=name" Doesn't work. Any help?</p>
</div>
<div id="comment-63408-info" class="comment-info">
<span class="comment-age">(10 May '18, 16:57)</span> <span class="comment-user userinfo">gfitz</span>
</div>
</div>
<span id="63409"></span>
<div id="comment-63409" class="comment">
<div id="post-63409-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It might help if you can clarify what end-result you're trying to get. What objects do you want, and which of those objects should have names?</p>
</div>
<div id="comment-63409-info" class="comment-info">
<span class="comment-age">(10 May '18, 19:28)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="63410"></span>
<div id="comment-63410" class="comment not_top_scorer">
<div id="post-63410-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Pretty much as the picture. Remove circled stuff while keeping everything else like roads rivers and such intact</p>
</div>
<div id="comment-63410-info" class="comment-info">
<span class="comment-age">(10 May '18, 20:13)</span> <span class="comment-user userinfo">gfitz</span>
</div>
</div>
<span id="63440"></span>
<div id="comment-63440" class="comment">
<div id="post-63440-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>@glitz you may have to split your data into &amp; remerge; i.e filter buildings, removing name into one file; put everything else into another, merge with osmconvert. Alternatively you could use osmosis with tag-transform.</p>
</div>
<div id="comment-63440-info" class="comment-info">
<span class="comment-age">(13 May '18, 12:41)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-63347" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-63347-form-container" class="comment-form-container">
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

<span id="63443"></span>

<div id="answer-container-63443" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63443-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63443-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-63443-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Load what you want into a database. Remove the names you want. That's it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 May '18, 16:47</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 May '18, 21:50</strong> </span></p>
</div>
</div>
<div id="comments-container-63443" class="comments-container">
<span id="63445"></span>
<div id="comment-63445" class="comment">
<div id="post-63445-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>How? why doesn't dropping tag x= name= only remove the names only? what's the syntax to keep the polygons or boundaries intact?</p>
</div>
<div id="comment-63445-info" class="comment-info">
<span class="comment-age">(13 May '18, 19:33)</span> <span class="comment-user userinfo">gfitz</span>
</div>
</div>
<span id="63446"></span>
<div id="comment-63446" class="comment">
<div id="post-63446-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The point about loading it into a database is that you can then run SQL statements on it as complicated as you like to remove some names and not others, depending on any rules that you care to set yourself.</p>
<p>You haven't said in the question what you're actually trying to achieve here (i.e. what you're going to do with the data afterwards), but I'm guessing that this is a rendering question largely because <a href="https://help.openstreetmap.org/questions/63004/rendering-tiles-of-specific-state">your other question</a> was.</p>
</div>
<div id="comment-63446-info" class="comment-info">
<span class="comment-age">(13 May '18, 20:42)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="63448"></span>
<div id="comment-63448" class="comment">
<div id="post-63448-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry. AFAIK it was pretty clear what my goals were. It can't be any simpler. That's why we went to osmfilter and it seems to be doing the job almost perfectly. If there's a command to filter out ''name'' tags then why does it remove building polygons?</p>
<p>Why the need to go into SQL queries when osmfilter seems to be the right tool for this?</p>
</div>
<div id="comment-63448-info" class="comment-info">
<span class="comment-age">(13 May '18, 22:52)</span> <span class="comment-user userinfo">gfitz</span>
</div>
</div>
<span id="63449"></span>
<div id="comment-63449" class="comment">
<div id="post-63449-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>you don't understand the answer ... sql helps only, --keep is a valid option for osmfilter, which doesn't remove buildings. To get buildings, you will need buildings tags. If you remove these tags, the buildings cannot be identified anymore.</p>
</div>
<div id="comment-63449-info" class="comment-info">
<span class="comment-age">(13 May '18, 23:43)</span> <span class="comment-user userinfo">AntaC</span>
</div>
</div>
<span id="63450"></span>
<div id="comment-63450" class="comment">
<div id="post-63450-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So is it impossible to use osmfilter to remove name tags from [amenity= government= craft= building= man_made= landuse= club= shop= office= landuse= leisure=] while keeping everything else?</p>
</div>
<div id="comment-63450-info" class="comment-info">
<span class="comment-age">(14 May '18, 00:22)</span> <span class="comment-user userinfo">gfitz</span>
</div>
</div>
<span id="63451"></span>
<div id="comment-63451" class="comment not_top_scorer">
<div id="post-63451-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>take a small extract and try combinations of keep and drop. It is a chance to have osmconvert &amp; osmfilter</p>
</div>
<div id="comment-63451-info" class="comment-info">
<span class="comment-age">(14 May '18, 01:28)</span> <span class="comment-user userinfo">AntaC</span>
</div>
</div>
<span id="63464"></span>
<div id="comment-63464" class="comment not_top_scorer">
<div id="post-63464-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Already tried with the command that's in the question and it almost works. There must be a keep= syntax to keep all polygons that am missing.</p>
</div>
<div id="comment-63464-info" class="comment-info">
<span class="comment-age">(14 May '18, 14:42)</span> <span class="comment-user userinfo">gfitz</span>
</div>
</div>
<span id="63471"></span>
<div id="comment-63471" class="comment not_top_scorer">
<div id="post-63471-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/14985/gfitz"></a><a href="https://help.openstreetmap.org/users/14985/gfitz">@gfitz</a> this program is a gift from its author. You can order to companies the perfect tool you need</p>
</div>
<div id="comment-63471-info" class="comment-info">
<span class="comment-age">(14 May '18, 15:55)</span> <span class="comment-user userinfo">AntaC</span>
</div>
</div>
<span id="63472"></span>
<div id="comment-63472" class="comment not_top_scorer">
<div id="post-63472-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Why does it sound like am asking for something super complex? remove only name tags from x keys.</p>
</div>
<div id="comment-63472-info" class="comment-info">
<span class="comment-age">(14 May '18, 16:18)</span> <span class="comment-user userinfo">gfitz</span>
</div>
</div>
</div>
<div id="comment-tools-63443" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-63443-form-container" class="comment-form-container">
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

