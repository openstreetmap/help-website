+++
type = "question"
title = "Render a static image (png, jpg...) of a map with a lightweight toolchain"
description = '''I am looking for a really simple thing: Getting a image of a map. I already found some solutions like using openlayers and capturing a screenshot of a openlayers site with phantom js (requires qt) or a solution like the one posted here: https://help.openstreetmap.org/questions/23034/maps-to-static-i...'''
date = "2014-05-23T09:24:00Z"
lastmod = "2014-05-23T14:46:00Z"
weight = 33398
keywords = [ "openstreetmap", "mapimage", "image", "png", "map" ]
aliases = [ "/questions/33398" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Render a static image (png, jpg...) of a map with a lightweight toolchain](/questions/33398/render-a-static-image-png-jpg-of-a-map-with-a-lightweight-toolchain)

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
<span id="post-33398-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33398-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33398-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am looking for a really simple thing: Getting a image of a map. I already found some solutions like using openlayers and capturing a screenshot of a openlayers site with phantom js (requires qt) or a solution like the one posted here: <a href="/questions/23034/maps-to-static-image-to-be-stored-on-a-mobile-application">https://help.openstreetmap.org/questions/23034/maps-to-static-image-to-be-stored-on-a-mobile-application</a> But this uses Mapnik, which has a bunch of dependencies. Since I want to generate the mapimages on a slim <strong>ARM</strong> linux, I need a much more lightweight solution, with less dependencies.</p>
<p>Any ideas? :)</p>
<p>Edit: So what do I want to achieve?</p>
<ul>
<li>Map should be offline accessible</li>
<li>Display a map with markers and polygons in a mobile QtQuick Application</li>
<li>-&gt; QtQuick Application can't render html files (because it runs on android)</li>
<li>-&gt; My idea for displaying maps: The app communicates with an arm linux machine (which is already used for the app), which sends preprocessed pictures of the currently needed map.</li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-mapimage" rel="tag" title="see questions tagged &#39;mapimage&#39;">mapimage</span> <span class="post-tag tag-link-image" rel="tag" title="see questions tagged &#39;image&#39;">image</span> <span class="post-tag tag-link-png" rel="tag" title="see questions tagged &#39;png&#39;">png</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 May '14, 09:24</strong></p>
<img src="https://secure.gravatar.com/avatar/36bc387102d2bd2d4c2809d50b2525dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DerMas&#39;s gravatar image" />
<p><span>DerMas</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DerMas has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 May '14, 15:21</strong> </span></p>
</div>
</div>
<div id="comments-container-33398" class="comments-container">
<span id="33399"></span>
<div id="comment-33399" class="comment">
<div id="post-33399-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is style of "the map" something that you will create yourself, or an existing one?</p>
</div>
<div id="comment-33399-info" class="comment-info">
<span class="comment-age">(23 May '14, 09:31)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="33400"></span>
<div id="comment-33400" class="comment">
<div id="post-33400-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I can use an existing style. Only custom thing I would like to do is to add markers and maybe polygons to the map.</p>
</div>
<div id="comment-33400-info" class="comment-info">
<span class="comment-age">(23 May '14, 09:55)</span> <span class="comment-user userinfo">DerMas</span>
</div>
</div>
<span id="33418"></span>
<div id="comment-33418" class="comment">
<div id="post-33418-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Perhaps it would help to take a step back and explain what problem it is that you're trying to solve? So far we know that it involves creating images involving a standard map style overlaid with markers and maybe polygons. We don't know if it has to be automated in some way, or where the "slim ARM linux" fits in (an ARM architecture would just perhaps require more stuff to be built from source, no?).</p>
</div>
<div id="comment-33418-info" class="comment-info">
<span class="comment-age">(23 May '14, 14:14)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="33419"></span>
<div id="comment-33419" class="comment">
<div id="post-33419-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, adding it to the question.</p>
</div>
<div id="comment-33419-info" class="comment-info">
<span class="comment-age">(23 May '14, 14:46)</span> <span class="comment-user userinfo">DerMas</span>
</div>
</div>
</div>
<div id="comment-tools-33398" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33398-form-container" class="comment-form-container">
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

<span id="33412"></span>

<div id="answer-container-33412" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33412-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33412-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-33412-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Our <a href="https://wiki.openstreetmap.org/wiki/Rendering">wiki page about Rendering</a> lists a few options. MapWeaver, for example, is a somewhat niche rendering engine that might fit your needs. Be aware that the least "lightweight" thing about all this will likely be to grab the data - it sounds like you would not want to have a 25 GB planet file lying around, much less keep the world's geodata available in a database. If you don't have the data locally then you will need to download it from a server whenever you want to generate a map, and that would then limit your options because you'd be placing load on the server.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 May '14, 12:18</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-33412" class="comments-container">
<span id="33413"></span>
<div id="comment-33413" class="comment">
<div id="post-33413-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Sounds great, will look into it :)</p>
<p>I have only tiles of certain areas, so that shouldn't be a problem.</p>
<p>edit: Unfortunately pearl doesn't work on the system :/ Python would work though, but I looked at the wiki page you mentioned and couldn't find a still maintained python project.</p>
</div>
<div id="comment-33413-info" class="comment-info">
<span class="comment-age">(23 May '14, 12:59)</span> <span class="comment-user userinfo">DerMas</span>
</div>
</div>
<span id="33414"></span>
<div id="comment-33414" class="comment">
<div id="post-33414-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Is it so hard to get perl working on your system?</p>
</div>
<div id="comment-33414-info" class="comment-info">
<span class="comment-age">(23 May '14, 13:40)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="33416"></span>
<div id="comment-33416" class="comment">
<div id="post-33416-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It is and I saw that mapweaver uses .osm files as input, which won't work for me also.</p>
</div>
<div id="comment-33416-info" class="comment-info">
<span class="comment-age">(23 May '14, 14:06)</span> <span class="comment-user userinfo">DerMas</span>
</div>
</div>
</div>
<div id="comment-tools-33412" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33412-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="33401"></span>

<div id="answer-container-33401" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33401-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33401-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33401-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'd probably use a <a href="http://switch2osm.org/using-tiles/getting-started-with-leaflet/">Leaflet-based map</a> for that. <a href="http://leafletjs.com/">Leaflet</a>'s small enough so that it'll fit happily in a mobile phone app, for example, so your "slim Linux" option should be possible too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 May '14, 10:28</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-33401" class="comments-container">
<span id="33402"></span>
<div id="comment-33402" class="comment">
<div id="post-33402-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not sure if I understand the getting started page of leaflet correct, but doesnt that just create a html map object instead of a static png image? I really need an image, which I can send to other machines, that cant render html pages. But maybe I have overlooked something. Could you give me a little push into the right direction?</p>
</div>
<div id="comment-33402-info" class="comment-info">
<span class="comment-age">(23 May '14, 10:42)</span> <span class="comment-user userinfo">DerMas</span>
</div>
</div>
<span id="33403"></span>
<div id="comment-33403" class="comment">
<div id="post-33403-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I was assuming that you'd be able to take a screenshot of the HTML map (with standard background, and things such as markers drawn on it).</p>
</div>
<div id="comment-33403-info" class="comment-info">
<span class="comment-age">(23 May '14, 10:43)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="33409"></span>
<div id="comment-33409" class="comment">
<div id="post-33409-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That would involve using phantomJS and qt (maybe there are other lightweight tools for taking screenshots of a html page?). I forgot to mention, that it is not only a lightweight linux, it is also an ARM machine.</p>
</div>
<div id="comment-33409-info" class="comment-info">
<span class="comment-age">(23 May '14, 11:21)</span> <span class="comment-user userinfo">DerMas</span>
</div>
</div>
</div>
<div id="comment-tools-33401" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33401-form-container" class="comment-form-container">
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

