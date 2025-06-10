+++
type = "question"
title = "Edit map for mobile App"
description = '''Hi! Today I was integrating OSM to an App and it&#x27;s already working, displaying my location and allowing me to move the map and control zoom by finger taps and pinches. BUT, now I need to add some elements to the map to be displayed, as POIs. Should I use external editors like OpenLayers or can I use...'''
date = "2013-01-09T21:57:00Z"
lastmod = "2013-01-10T15:13:00Z"
weight = 18943
keywords = [ "android", "ios", "poi" ]
aliases = [ "/questions/18943" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Edit map for mobile App](/questions/18943/edit-map-for-mobile-app)

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
<span id="post-18943-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18943-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18943-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi! Today I was integrating OSM to an App and it's already working, displaying my location and allowing me to move the map and control zoom by finger taps and pinches. BUT, now I need to add some elements to the map to be displayed, as POIs. Should I use external editors like OpenLayers or can I use OSM maps editors (Potlatch &amp; JOSM) and then display the edited map in the App?</p>
<p>I'm developing the App in Unity, for iOS and Android, and accessing the map via:</p>
<p>///string dlUrl = String.Format("http://tile.openstreetmap.org/{0}/{1}/{2}.png", zoomLevel, (int) tileId.x, (int) tileId.y);///</p>
<p>so I guess I could access an edited map using it's URL, but I don't know if OSM give the URL to an edited map.</p>
<p>Any help will be welcome, Thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-ios" rel="tag" title="see questions tagged &#39;ios&#39;">ios</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jan '13, 21:57</strong></p>
<img src="https://secure.gravatar.com/avatar/c13f706d83e6363a2832d754da0b15da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alchemy3D&#39;s gravatar image" />
<p><span>Alchemy3D</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alchemy3D has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-18943" class="comments-container">
<span id="18944"></span>
<div id="comment-18944" class="comment">
<div id="post-18944-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just to clarify, when you say "now I need to add some elements to the map to be displayed" do you mean you want to display POIs from some non-OSM source, or do you mean you want to add these POIs to OSM (and then display them)?</p>
<p>Because OpenStreetMap is just one giant lump of data, anything that you add to it needs to (a) really exist in the real world and (b) be licence compatible.</p>
<p>Perhaps if you could give a few more details we'd understand a bit more about what you're trying to do?</p>
</div>
<div id="comment-18944-info" class="comment-info">
<span class="comment-age">(09 Jan '13, 22:06)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="18947"></span>
<div id="comment-18947" class="comment">
<div id="post-18947-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Sure! sorry. I'm working in a medical App that will show institutions where professionals can renew their medical certificates. OSM doesn't have those entries and it will be a list of hundreds/thousands of them so I'm not sure it would be useful to add them to OSM, so if only the App can display them I will be more than satisfied.</p>
</div>
<div id="comment-18947-info" class="comment-info">
<span class="comment-age">(09 Jan '13, 22:35)</span> <span class="comment-user userinfo">Alchemy3D</span>
</div>
</div>
</div>
<div id="comment-tools-18943" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18943-form-container" class="comment-form-container">
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

<span id="18966"></span>

<div id="answer-container-18966" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18966-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18966-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18966-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Several points about what you are trying to do:</p>
<ul>
<li><p>you cannot simply reuse OSM tile server resources for your mobile app. There is a "<a href="http://wiki.openstreetmap.org/wiki/Tile_usage_policy">Tile server usage policy</a>" defined in the wiki. Rendering and delivering map tiles is not free and OSM is a non-profit organisation with limited resources. You can find alternative OSM tiles providers on the referenced wiki page.</p></li>
<li><p>be careful about the OSM license ODbL. Don't mix your dataset with OSM dataset. Check the <a href="http://wiki.openstreetmap.org/wiki/Legal_FAQ#3c._If_I_make_something_with_OSM_data.2C_do_I_now_have_to_apply_your_license_to_my_whole_work.3F">Legal FAQ</a> and related wiki pages about the license.</p></li>
</ul>
<p>The best for you is to create an overlay either rendered locally on the mobile or through your own web server and with OSM map in background.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jan '13, 13:09</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jan '13, 14:29</strong> </span></p>
</div>
</div>
<div id="comments-container-18966" class="comments-container">
<span id="18970"></span>
<div id="comment-18970" class="comment">
<div id="post-18970-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Pieren, I found the alternative tile servers you are talking about and I will use a free one for sure. When you say to create an overlay to be rendered on top of a OSM map you are coming back to my question. I don't know how to do it, could you give me a clue? All the documentation I found is about using layers in websites by html, but I need those layers to be displayed inside an App in Android and iOS devices. That's why I was wondering if it could be done with OSM editors. Thanks!</p>
</div>
<div id="comment-18970-info" class="comment-info">
<span class="comment-age">(10 Jan '13, 15:08)</span> <span class="comment-user userinfo">Alchemy3D</span>
</div>
</div>
<span id="18971"></span>
<div id="comment-18971" class="comment">
<div id="post-18971-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's going to depend on the toolkit that you're using. There's an <a href="http://switch2osm.org/using-tiles/getting-started-with-leaflet/">example</a> on the switch2osm site using <a href="http://leafletjs.com/">Leaflet</a> (a JavaScript-based toolkit). Since you're using Unity, perhaps there are some support forums for that (or a help site somewhere)?</p>
</div>
<div id="comment-18971-info" class="comment-info">
<span class="comment-age">(10 Jan '13, 15:13)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-18966" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18966-form-container" class="comment-form-container">
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

