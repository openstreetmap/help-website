+++
type = "question"
title = "Newbie- getting started, one random place with specific tag"
description = '''Hi, I want to create a web app that has a form to search amenities/places by tags, and after entering a tag it would show on map one random place with that tag. I was told I could use for that leaflet.js and OpenStreetMap API, but as I am completely new to that, I have no idea where I should start. ...'''
date = "2020-03-22T19:51:00Z"
lastmod = "2020-03-25T20:33:00Z"
weight = 73684
keywords = [ "random", "newbie", "tags" ]
aliases = [ "/questions/73684" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Newbie- getting started, one random place with specific tag](/questions/73684/newbie-getting-started-one-random-place-with-specific-tag)

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
<span id="post-73684-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73684-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73684-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I want to create a web app that has a form to search amenities/places by tags, and after entering a tag it would show on map one random place with that tag. I was told I could use for that leaflet.js and OpenStreetMap API, but as I am completely new to that, I have no idea where I should start. I've searched for tutorials but I couldn't find anything, except overpass seems to have the tags I am looking for. I have successfully added a leaflet map to my page and now I have no idea what to do next. Can anyone please point me to some tutorials or documents that would help me with getting started?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-random" rel="tag" title="see questions tagged &#39;random&#39;">random</span> <span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Mar '20, 19:51</strong></p>
<img src="https://secure.gravatar.com/avatar/86ca9330c13ba50e8ea187c3dd76386a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Monilus98&#39;s gravatar image" />
<p><span>Monilus98</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Monilus98 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Mar '20, 20:09</strong> </span></p>
</div>
</div>
<div id="comments-container-73684" class="comments-container">
&#10;</div>
<div id="comment-tools-73684" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73684-form-container" class="comment-form-container">
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

<span id="73686"></span>

<div id="answer-container-73686" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73686-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73686-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-73686-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi</p>
<p>Firstly, your project is much more complicated that it looks like, there is a lot of data to process. And I don't really see the point, but anyway.</p>
<p>To get the list of tags to choose from, I would ask Taginfo. Either through the <a href="https://wiki.openstreetmap.org/wiki/Taginfo/API">API</a>, or through <a href="https://taginfo.openstreetmap.org/download">downloads</a>. Read carefully the limits of the API. If you limit yourself the amenity and place keys, you can do requests like these to find the associated values (<a href="https://taginfo.openstreetmap.org/taginfo/apidoc#api_4_key_values">doc</a>) :</p>
<p><a href="https://taginfo.openstreetmap.org/api/4/key/values?key=place&amp;page=1&amp;rp=10&amp;sortname=count_ways&amp;sortorder=desc">https://taginfo.openstreetmap.org/api/4/key/values?key=place&amp;page=1&amp;rp=10&amp;sortname=count_ways&amp;sortorder=desc</a></p>
<p>Please handle the pagination, there is already 1417 results for this request (about place) and amenity is worse !</p>
<p>Once you have a specific tag selected comes the biggest problem, finding one random object with this tag. With Overpass you can limit the results set to 1, but only after having fully computed it. If you try to search for common tags in the whole world, you'll get timeouts.</p>
<p>One solution could be to compute random (not too big) bounding boxes, and then use this kind of <a href="https://overpass-turbo.eu/s/RP8">request</a>. nwr means looks for node or ways or relations. You'll need to replace {{bbox}} by your computed bounding box (try not to look in the water). "out center" means to output a node, even if the result was a way or a relation. And 1 limits to the first result. You might want to get the full results, and randomize there.</p>
<p>Be gentle with the overpass server, if you want to retry another bounding box when no results, wait a little between requests, or you'll get blocked.</p>
<p>To display the results of your overpass query, have a look at this <a href="https://github.com/GuillaumeAmat/leaflet-overpass-layer">leaflet plugin</a> (not tested myself).</p>
<p>Hope this helps, good luck with your project.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Mar '20, 00:07</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-73686" class="comments-container">
<span id="73709"></span>
<div id="comment-73709" class="comment">
<div id="post-73709-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you so much for your answer, I'll definitely look into this stuff :) After I've started to look into how to do that I had a feeling it would be really complicated but I can't really back out now, so I'm stuck with this project... But I have been thinking about how to make it a bit easier without changing the concept too much, so I've been wondering- would limiting the number of searchable tags and the area to just one town be possible and if yes would it make the task easier or just even more complicated? Thanks again :)</p>
</div>
<div id="comment-73709-info" class="comment-info">
<span class="comment-age">(23 Mar '20, 15:24)</span> <span class="comment-user userinfo">Monilus98</span>
</div>
</div>
<span id="73713"></span>
<div id="comment-73713" class="comment">
<div id="post-73713-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sure, a hand-curated list of tags (from the <a href="https://wiki.openstreetmap.org/wiki/Map_Features">wiki</a> for example, or from the top list of <a href="https://taginfo.openstreetmap.org/tags">taginfo</a>) will be easier to manage than 10000+ results, with some tags used only once in the whole world ! ;-)</p>
<p>And if you limit your Overpass queries to a town, it should be okay for the server. See this <a href="https://overpass-turbo.eu/s/RQF">request</a> for the query in one town (Berlin). As before, you can limit the resulting set to 1, but it seems it will always be the same one, probably not what you want.</p>
<p>I think that with the mentioned leaflet plugin, you can use the onSuccess callback to randomize and filter the results before display.</p>
<p>I see that by default this plugin use the bbox to limit the query, you could use that instead of limiting to a town. For example you limit the minimum zoom of your map, so the displayed area will never be too big, and you run your request on the visible area. Thus users can change area themselves.</p>
<p>Remember that sometimes there will be no results, you should not fail silently IMHO.</p>
<p>I'd be curious to see the result of your work, if possible ! ;-)</p>
<p>Regards.</p>
</div>
<div id="comment-73713-info" class="comment-info">
<span class="comment-age">(23 Mar '20, 18:18)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="73734"></span>
<div id="comment-73734" class="comment">
<div id="post-73734-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks again! If I'll be able to finish it I'll show you as soon as it's done :)</p>
</div>
<div id="comment-73734-info" class="comment-info">
<span class="comment-age">(24 Mar '20, 19:29)</span> <span class="comment-user userinfo">Monilus98</span>
</div>
</div>
<span id="73753"></span>
<div id="comment-73753" class="comment">
<div id="post-73753-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi again, this is a bit embarrassing after all this time, but as much as I understand the logic behind what I have to do, I actually have no idea how to use the overpass api. I get that I can run queries and get results in overpass turbo, but how do I do that on my own website? Do I install it on my server or somehow call in in the javascript file? I really am a total newbie to this so I'm sorry for this kind of silly question, but for some reason I can't find any tutorial that shows how to do it...</p>
</div>
<div id="comment-73753-info" class="comment-info">
<span class="comment-age">(25 Mar '20, 19:56)</span> <span class="comment-user userinfo">Monilus98</span>
</div>
</div>
<span id="73755"></span>
<div id="comment-73755" class="comment">
<div id="post-73755-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Well, running an overpass query is just loading a specific URL. Overpass Turbo provides a web interfaces to test your queries and see the results. Once your query does what you want, you don't need it anymore. Just use the "Export -&gt; Query -&gt; compact" menu to get the corresponding URL.</p>
<p>You said you used leaflet to display a map. As said before, you can use this <a href="https://github.com/GuillaumeAmat/leaflet-overpass-layer">plugin</a> to load an Overpass query's result and display it on top of your map. Have a look at the <a href="https://github.com/GuillaumeAmat/leaflet-overpass-layer/blob/721930b5b63e78ac687a656ef6f65a873e1139ff/src/OverPassLayer.js#L22">onSuccess callback code</a>, to rewrite it for your needs, namely selecting a random result.</p>
<p>The doc says to use complicated thing like bower or npm to install the plugin, but I think that you just need to load the js and css for the dist folder on your page !</p>
<p>Digging into the <a href="https://leafletjs.com/reference-1.6.0.html">leaflet doc</a>, to understand how layers and plugins work, should prove useful.</p>
<p>Good luck.</p>
</div>
<div id="comment-73755-info" class="comment-info">
<span class="comment-age">(25 Mar '20, 20:33)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
</div>
<div id="comment-tools-73686" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73686-form-container" class="comment-form-container">
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

