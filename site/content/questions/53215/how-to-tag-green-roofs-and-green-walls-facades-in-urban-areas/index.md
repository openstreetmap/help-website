+++
type = "question"
title = "how to tag green roofs and green walls (façades) in urban areas?"
description = '''Hello OSM Community! New here and wanting to tag green roofs and green walls (separately - particularly in Berlin, Germany). There does not seem to be tags for these elements yet - how do I go about creating a new tag for this? Should also distinguish between public/private areas...  Best, Samie'''
date = "2016-12-02T10:13:00Z"
lastmod = "2016-12-09T21:36:00Z"
weight = 53215
keywords = [ "greenwalls", "greenroof", "greenspace" ]
aliases = [ "/questions/53215" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [how to tag green roofs and green walls (façades) in urban areas?](/questions/53215/how-to-tag-green-roofs-and-green-walls-facades-in-urban-areas)

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
<span id="post-53215-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53215-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-53215-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello OSM Community!</p>
<p>New here and wanting to tag green roofs and green walls (separately - particularly in Berlin, Germany). There does not seem to be tags for these elements yet - how do I go about creating a new tag for this? Should also distinguish between public/private areas...</p>
<p>Best, Samie</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-greenwalls" rel="tag" title="see questions tagged &#39;greenwalls&#39;">greenwalls</span> <span class="post-tag tag-link-greenroof" rel="tag" title="see questions tagged &#39;greenroof&#39;">greenroof</span> <span class="post-tag tag-link-greenspace" rel="tag" title="see questions tagged &#39;greenspace&#39;">greenspace</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Dec '16, 10:13</strong></p>
<img src="https://secure.gravatar.com/avatar/5c44d0d828fc850a9b3c4d8f5088ee5c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="essgame&#39;s gravatar image" />
<p><span>essgame</span><br />
<span class="score" title="71 reputation points">71</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="essgame has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53215" class="comments-container">
<span id="53216"></span>
<div id="comment-53216" class="comment">
<div id="post-53216-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Do you mean "roofs coloured green" or "roofs with plants growing on them"?</p>
</div>
<div id="comment-53216-info" class="comment-info">
<span class="comment-age">(02 Dec '16, 11:14)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="53435"></span>
<div id="comment-53435" class="comment">
<div id="post-53435-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So it looks liek there is no consensus at all on how to map/tag green roofs or façades.... how does one get an consensus on these things within the OSM community?</p>
<p>For now, I think I like:</p>
<p>roof:cover=plants wall:cover=plants</p>
<p>as I think it describes what we are looking for best. If I go with the above tag, where/how do I use it? (such a newbie, sorry for the basics...)</p>
<p>THANKS</p>
<p>xx Samie</p>
</div>
<div id="comment-53435-info" class="comment-info">
<span class="comment-age">(09 Dec '16, 09:48)</span> <span class="comment-user userinfo">essgame</span>
</div>
</div>
<span id="53444"></span>
<div id="comment-53444" class="comment">
<div id="post-53444-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/13042/essgame">@essgame</a> There's no precise definition for "consensus" in the OSM community, but looking at the wiki documentation and checking the popularity among mappers and developers (e.g. using <a href="http://taginfo.openstreetmap.org/">Taginfo</a> statistics) gets you pretty close.</p>
<p>The keys building:material and roof:material, which I mentioned in my answer, have together been used over a million times, and are supported by numerous data consumers. This is as close to established consensus as you will ever get in OSM.</p>
<p>The exact values to use for green roofs and walls (such as "grass" or "plants") are not really established yet, but introducing new keys won't help with that at all.</p>
</div>
<div id="comment-53444-info" class="comment-info">
<span class="comment-age">(09 Dec '16, 15:38)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
<span id="53445"></span>
<div id="comment-53445" class="comment">
<div id="post-53445-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Indeed follow <a href="http://help.openstreetmap.org/users/14/tordanik">@Tordanik</a>'s advice (&amp; if you feel inclined also additionally add one of the tags I suggest). These two approaches are compatible &amp; synergistic: roof:material &amp; building:material are widely used for 3D rendering, and values can be refined if actual composition of the plants is known, the green_roof tag allows one to find objects specifically known to be green roofs, whereas roof:material=plants may cover a wider range of roofs.</p>
</div>
<div id="comment-53445-info" class="comment-info">
<span class="comment-age">(09 Dec '16, 21:36)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-53215" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53215-form-container" class="comment-form-container">
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

<span id="53254"></span>

<div id="answer-container-53254" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53254-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53254-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-53254-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'll divide this answer into three parts, related to roof material, façade material, and individual rooftop plants, respectively.</p>
<h2 id="roof-material">Roof material</h2>
<p>When we look at the usage numbers of tags related to plants on roofs, the most common example is <code>roof:material=grass</code>, which is also documented on the <a href="https://wiki.openstreetmap.org/wiki/Key:roof:material"><code>roof:material</code></a> wiki page. A related, but much less common tag is <code>roof:material=plants</code>.</p>
<p>An important detail in this context is that the roof:material key itself is defined as the <em>"outer material for the building roof"</em>. So when there are multiple materials involved (which is commonly the case, such as with shingles on top of a wooden frame, a plaster coating on concrete etc.), we tag the outermost layer.</p>
<p>There are two main reasons why this definition was chosen:</p>
<ul>
<li>The key was invented (and is still mainly used) in the context of 3D rendering. For this use case, hidden layers of material are not interesting as they are not rendered.</li>
<li>The "core" materials involved in the construction of a building can, in many cases, not be verified on the ground.</li>
</ul>
<p>As such, tagging a plant-covered roof using roof:material is appropriate, even though there is likely a supporting structure made from some other material.</p>
<h2 id="façade-material">Façade material</h2>
<p>The <a href="https://wiki.openstreetmap.org/wiki/Key:building:material"><code>building:material</code></a> key is defined analogously to the <code>roof:material</code> key, so the same arguments apply.</p>
<p>However, this is not applicable to buildings only partially overgrown with plants (such as vines), as the material below is still visible in that case. As far as I know, there is no tag for this particular situation.</p>
<h2 id="rooftop-plants">Rooftop plants</h2>
<p>Roof gardens and other "green roofs" are not limited to grass, but can consist of many other plants, up to and including trees. You can map those normally, with tags such as <code>natural=tree</code>. In addition, I recommend adding a tag to tells applications that this plant is on the roof, such as <code>location=rooftop</code>. There's no really established practice for that, though.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Dec '16, 20:52</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-53254" class="comments-container">
&#10;</div>
<div id="comment-tools-53254" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53254-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53217"></span>

<div id="answer-container-53217" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53217-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53217-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53217-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Assuming the "roof/wall with <a href="https://en.wikipedia.org/wiki/Green_wall">plants growing on them</a>" definition.</p>
<p>I'd be tempted to go with <em>wall:cover:material</em> and <em>roof:cover:material</em> except that there's hardly any existing value that matches on <a href="http://taginfo.openstreetmap.org/search?q=material">taginfo</a>. There's <em>roof:material=grass/plants</em> with decent usage numbers, but green walls are usually covered by plants, not made from them.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Dec '16, 12:26</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-53217" class="comments-container">
<span id="53255"></span>
<div id="comment-53255" class="comment">
<div id="post-53255-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Even though the walls are only covered by plants, the existing keys building:material and roof:material still fit. They were intentionally defined as the outermost material when the tag was created, thus plaster (the second-most common value) or plants are right at home there. I've tried to elaborate a bit with my answer.</p>
</div>
<div id="comment-53255-info" class="comment-info">
<span class="comment-age">(05 Dec '16, 20:58)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-53217" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53217-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53256"></span>

<div id="answer-container-53256" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53256-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53256-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53256-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think Tordanik has covered the basic tagging issues.</p>
<p>However using roof:material and building:material keys do not unambiguously identify any given structure as being a green roof or wall. Indeed I can think of at least one building where the outer material of the roof is grass, but this is not a green roof. To avoid this I would suggest the use of one of:</p>
<ul>
<li>green_roof=yes or green_wall=yes</li>
<li>or man_made=green_roof, man_made=green_wall</li>
</ul>
<p>In practice green roofs and green walls usually only cover part of a roof or a single façade. Thus at least green roof tagging is often best combined with <a href="http://wiki.openstreetmap.org/wiki/Key:building:part">building:part</a></p>
<p>As I have stated elsewhere these are usually distinct structures from the building proper, but Tordanik clarifies that point.</p>
<p>In most cases roof:material=grass for a green roof will be wrong, but it is difficult to ascertain the actual composition of the plants used in the green roof. Many green roofs will have different mixes of plants in zones across the roof:</p>
<p><img src="http://s0.geograph.org.uk/geophotos/05/15/17/5151779_b4ce361d.jpg" alt="Green Roof Jubilee Campus" /></p>
<p>(my own image from <a href="http://www.geograph.org.uk/photo/5151779">Geograph</a>)</p>
<p>Incidentally the famous green wall at Caixa Forum, Madrid is mapped as a garden: <a href="http://www.geograph.org.uk/photo/5151779.">http://www.geograph.org.uk/photo/5151779.</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Dec '16, 09:43</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</img>
</div>
</div>
<div id="comments-container-53256" class="comments-container">
&#10;</div>
<div id="comment-tools-53256" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53256-form-container" class="comment-form-container">
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

