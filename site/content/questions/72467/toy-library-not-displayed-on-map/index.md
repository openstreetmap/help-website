+++
type = "question"
title = "Toy library not displayed on map"
description = '''The new amenity &quot;toy library&quot; isn&#x27;t displayed on OpenStreetMap despite being a node and having an specific icon since September according to the Wiki. I work in one of them and I hope someone knows how to fix it. I tried a lot of different locations and they are all invisible. Before the new amenity...'''
date = "2020-01-10T22:20:00Z"
lastmod = "2020-01-12T00:02:00Z"
weight = 72467
keywords = [ "toy_library", "icon" ]
aliases = [ "/questions/72467" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Toy library not displayed on map](/questions/72467/toy-library-not-displayed-on-map)

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
<span id="post-72467-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72467-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72467-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The new amenity "toy library" isn't displayed on OpenStreetMap despite being a node and having an specific icon since September according to the Wiki. I work in one of them and I hope someone knows how to fix it. I tried a lot of different locations and they are all invisible. Before the new amenity, they were classified as "library" and were properly displayed. On behalf of my coworkers, I hope you'll find ways to fix this issue. Jean</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-toy_library" rel="tag" title="see questions tagged &#39;toy_library&#39;">toy_library</span> <span class="post-tag tag-link-icon" rel="tag" title="see questions tagged &#39;icon&#39;">icon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jan '20, 22:20</strong></p>
<img src="https://secure.gravatar.com/avatar/8e33d10de493761278f4a77df7b8e7c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jeanmelo&#39;s gravatar image" />
<p><span>Jeanmelo</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jeanmelo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72467" class="comments-container">
&#10;</div>
<div id="comment-tools-72467" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72467-form-container" class="comment-form-container">
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

<span id="72469"></span>

<div id="answer-container-72469" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72469-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72469-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-72469-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What appears to have happened is that someone <a href="https://lists.openstreetmap.org/pipermail/tagging/2019-October/048509.html">noticed</a> that the tag was sort-of in use but had never been voted on in the wiki, arranged a <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/toy_library">vote</a> which no-one objected to and then left things at that.</p>
<p>Unfortunately, a wiki page does not magically tell people who look after renderers that there's a tag they probably need to consider. The place to do that for the map layer shown on OpenStreetMap.org as the "standard" layer would be <a href="https://github.com/gravitystorm/openstreetmap-carto/search?q=toy+library&amp;unscoped_q=toy+library">here</a>, and it looks like no-one has mentioned it. The people in charge of that map style may consider that 283 uses worldwide is still a bit low to consider for inclusion, but if it was to be included, someone would basically have to go through a process similar to the one that I wrote up in <a href="https://www.openstreetmap.org/user/SomeoneElse/diary/43041">this</a> diary entry. Adding a new amenity to the style is about the simplest change you can make so it'd be a really good "first issue" for someone to have a go at.</p>
<p>Other map styles would also need to be updated by whoever maintains them (now that you've asked this question I'll update the <a href="https://map.atownsend.org.uk/maps/map/map.html">one</a> that I look after - probably by just rendering it as a default leisure or amenity item). Normally I'd get prodded into doing this by seeing a posting on the tagging list saying that voting has closed, but I don't see a posting after <a href="https://lists.openstreetmap.org/pipermail/tagging/2019-October/048722.html">this one</a>.</p>
<p>I can see that people are actively using the new scheme (see <a href="https://www.openstreetmap.org/node/454568376/history">here</a> for example). Although that edit did have the effect of removing the display of a feature from displayed maps, I actually think that that edit (the change from "library" to "toy_library") makes sense because it was mistagged beforehand; it wasn't what anyone would call a normal "library".</p>
<p>If you'd like to have a go at adding the rendering of "toy_library" to OSM's "standard" map style then I'd suggest you create a new issue there about it and say you'd like to have a go at updating the style as well. If people think that <a href="https://taginfo.openstreetmap.org/tags/amenity=toy_library">usage</a> isn't really high enough yet then create an issue at my style <a href="https://github.com/SomeoneElseOSM/SomeoneElse-style">here</a> and I'll help you through the process.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jan '20, 22:48</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jan '20, 22:51</strong> </span></p>
</div>
</div>
<div id="comments-container-72469" class="comments-container">
<span id="72475"></span>
<div id="comment-72475" class="comment">
<div id="post-72475-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your complete and really quick answer. I now understand why it's not displayed on the standard OSM style. I see that someone have already created an issue on GitHub in last June (<a href="https://github.com/gravitystorm/openstreetmap-carto/issues/3803">https://github.com/gravitystorm/openstreetmap-carto/issues/3803</a>) and that the rendering team has refused to display it until it has more than 1000 uses worldwide, which seems doable if more toy libraries were correctly tagged. I'll try for the time being to add more locations that I know about before asking. I'll contact you in some time to add the rendering in your map style if I am free.</p>
<p>Thank you for your time! Jean</p>
</div>
<div id="comment-72475-info" class="comment-info">
<span class="comment-age">(12 Jan '20, 00:02)</span> <span class="comment-user userinfo">Jeanmelo</span>
</div>
</div>
</div>
<div id="comment-tools-72469" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72469-form-container" class="comment-form-container">
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

