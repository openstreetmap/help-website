+++
type = "question"
title = "Creating a collaborative community map (another personalised map question!)"
description = '''I&#x27;ve seen some posts about personalised maps but have got a bit lost with some of the the functionality of different options (tiles, vectors... Beyond me!). Also some of those posts are quite old and I don&#x27;t know if there are any new solutions. I am working on a community project where I would like ...'''
date = "2021-03-15T09:34:00Z"
lastmod = "2021-03-16T07:41:00Z"
weight = 79257
keywords = [ "layers", "newbie", "community", "collaborative", "personalised" ]
aliases = [ "/questions/79257" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Creating a collaborative community map (another personalised map question!)](/questions/79257/creating-a-collaborative-community-map-another-personalised-map-question)

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
<span id="post-79257-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79257-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79257-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've seen some posts about personalised maps but have got a bit lost with some of the the functionality of different options (tiles, vectors... Beyond me!). Also some of those posts are quite old and I don't know if there are any new solutions.</p>
<p>I am working on a community project where I would like to map local green spaces, which I have started doing through OSM (adding names of parks, woodland etc). I would then like to add various layers - highlighting walking routes between green spaces, or adding things like details of volunteer projects and activities. This is where I would need a personalised map that could be embedded on a website, shared on social media etc.</p>
<p>The next thing I would like to do is have layers which the community could contribute to. For example, with Spring coming up then I will be running a campaign to encourage people to take photos of wildflowers they see while they are out walking. It would be great if people could upload those directly to a map, rather than sending them to me and then me adding them.</p>
<p>I have seen uMap, Leaflet, MapHub, OpenLayers, Mapbox, Maperitive... I don't know if any or all of these would meet the needs outlined above. If anyone could advise on these or alternative solutions I would appreciate it! I would also be open to trying to seek funding for a paid solution, but I don't really know where to start, what type of professional to speak to etc.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-layers" rel="tag" title="see questions tagged &#39;layers&#39;">layers</span> <span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span> <span class="post-tag tag-link-community" rel="tag" title="see questions tagged &#39;community&#39;">community</span> <span class="post-tag tag-link-collaborative" rel="tag" title="see questions tagged &#39;collaborative&#39;">collaborative</span> <span class="post-tag tag-link-personalised" rel="tag" title="see questions tagged &#39;personalised&#39;">personalised</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Mar '21, 09:34</strong></p>
<img src="https://secure.gravatar.com/avatar/c96c8c0a174f4693bca57adadf24dc7f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="frodshamroots&#39;s gravatar image" />
<p><span>frodshamroots</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="frodshamroots has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Mar '21, 09:38</strong> </span></p>
</div>
</div>
<div id="comments-container-79257" class="comments-container">
&#10;</div>
<div id="comment-tools-79257" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79257-form-container" class="comment-form-container">
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

<span id="79268"></span>

<div id="answer-container-79268" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79268-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79268-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-79268-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="frodshamroots has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello,</p>
<p>I would start with <a href="https://wiki.openstreetmap.org/wiki/UMap">uMap</a> which would fit most of your needs. On top of a basemap, you can draw lines, points and such, pull data from the OSM database (like paths or parks) using <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">overpass</a> to highlight them (with mapCSS styling) and add a layer with photos. The awkward part will be the collaborative stuff, as user management is crude. Mainly you share editing rights with some user, who will be able to break everything, especially if they are not familiar with the software.</p>
<p>You could pull the images from an external database, for example powered with a gallery software, like <a href="https://www.piwigo.org/">piwigo</a> which has a plugin enabling users to add or correct the geo-location of photos. It should be trivial to automatically export a csv list of all the images, which you would then pull into uMap as a specific layer.</p>
<p>You could also use a software like <a href="https://gitlab.adullact.net/pixelhumain/GoGoCarto">GoGoCarto</a>, which was made especially for cartographic collaboration. It has user-friendly forms to add points, admin or community-driven moderation, and such. But I don't think you can freely draw stuff, or pull data from OSM. You might be able to pull GoGoCarto data from uMap as one layer though.</p>
<p>I don't know MapHub, it seems closed-source.</p>
<p>Leaflet and OpenLayers are js framework to create cartographic web applications. It would be a good building block should you start coding something from scratch.</p>
<p>Maperitive is used to produced raster maps from OSM data, not what you are looking for I think. Mapbox main product has to same aim, but they offer a lot of other services, mostly closed-source though.</p>
<p>If you want to display existing walking routes, you could use <a href="https://hiking.waymarkedtrails.org/">Waymarked Trails</a> hiking layer, on top of any basemap you'd like. It only shows official hiking routes mapped in OSM though.</p>
<p>Anyway, you should begin by reading the documentation of the mentioned tools, the OSM wiki is full of information, and test them, to see if you can tweak them to your needs.</p>
<p>Hope this help. Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Mar '21, 14:36</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-79268" class="comments-container">
<span id="79283"></span>
<div id="comment-79283" class="comment">
<div id="post-79283-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That certainly does help, thank you very much :)</p>
</div>
<div id="comment-79283-info" class="comment-info">
<span class="comment-age">(16 Mar '21, 07:41)</span> <span class="comment-user userinfo">frodshamroots</span>
</div>
</div>
</div>
<div id="comment-tools-79268" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79268-form-container" class="comment-form-container">
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

