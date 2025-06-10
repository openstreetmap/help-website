+++
type = "question"
title = "How do I use my new style (OSM.xml) file to generate new tiles"
description = '''I have searched for weeks on how to change my map style and have finally got an OSM.xml file (generated from OSM-Bright theme with Tilemill etc, that I am happy with here: https://googledrive.com/host/0B6Lb5ThDkG8ZakR2OXJHTDRQUUk My tile server is using the exact steps shown here: http://switch2osm....'''
date = "2014-06-08T01:29:00Z"
lastmod = "2014-06-08T21:36:00Z"
weight = 33784
keywords = [ "osm.xml", "mapnik", "mod_tile" ]
aliases = [ "/questions/33784" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How do I use my new style (OSM.xml) file to generate new tiles](/questions/33784/how-do-i-use-my-new-style-osmxml-file-to-generate-new-tiles)

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
<span id="post-33784-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33784-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33784-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have searched for weeks on how to change my map style and have finally got an OSM.xml file (generated from OSM-Bright theme with Tilemill etc, that I am happy with here: <a href="https://googledrive.com/host/0B6Lb5ThDkG8ZakR2OXJHTDRQUUk">https://googledrive.com/host/0B6Lb5ThDkG8ZakR2OXJHTDRQUUk</a></p>
<p>My tile server is using the exact steps shown here: <a href="http://switch2osm.org/">http://switch2osm.org/</a> the server can be seen here: <a href="http://osmtileserver.cloudapp.net/osm/slippymap.html?zoom=11&amp;lat=-39.44448&amp;lon=176.85734&amp;layers=B0">http://osmtileserver.cloudapp.net/osm/slippymap.html?zoom=11&amp;lat=-39.44448&amp;lon=176.85734&amp;layers=B0</a></p>
<p>I have been searching for how I can update the styling of my tiles but with no luck. I assume I need to replace the osm.xml file with my new one; however it doesn't work (instead I get a mixture of out of date tiles and pink tiles (pink where the tile image isn't loading).</p>
<p>Could this be because my OSM.xml file is invalid? If so how can I get logs for the issue at hand? Am I following the correct way to replace a style?</p>
<p>I have tried to use the url method for marking tiles as dirty but it appears to not do anything. I have also have two ubuntu installs (one locally in hyper-v and the other one is the one linked. I have tried on both, with the same result).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm.xml" rel="tag" title="see questions tagged &#39;osm.xml&#39;">osm.xml</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jun '14, 01:29</strong></p>
<img src="https://secure.gravatar.com/avatar/ffe8ab5bc0cb86bd1cb53167b02529c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dessus&#39;s gravatar image" />
<p><span>Dessus</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dessus has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Jun '14, 08:13</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-33784" class="comments-container">
&#10;</div>
<div id="comment-tools-33784" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33784-form-container" class="comment-form-container">
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

<span id="33787"></span>

<div id="answer-container-33787" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33787-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33787-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-33787-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Dessus has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please run renderd with the -f flag (instead of starting it via an init script) you should then see what ever is going wrong.</p>
<p>One of the common problems when using a TileMill generated style is that it generates one that is valid for a more recent version of Mapnik than the installed one. A frequent issue is that older version do not support the "Parameters" section, which you can simply delete. further you need to check if the values in the "Datasource" section (access config for your DB) are correct for your server installation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jun '14, 08:12</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Jun '14, 08:14</strong> </span></p>
</div>
</div>
<div id="comments-container-33787" class="comments-container">
<span id="33790"></span>
<div id="comment-33790" class="comment">
<div id="post-33790-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How can I upgrade my Mapnik version (I am new to linux etc). Do I use the apt-get command?</p>
<p>You have hit the issue on the head in that I do have errors around the parameters section (which is kinda expected I guess, considering that they have windows file paths etc). Is it better to upgrade my mapnik? or is it better to just remove the parameters.</p>
<p>Am I making things more difficult for myself by using Tilemill in windows? The thing that is i guess confusing me is that the OSM-Bright project seems to link 3 files into tile mill from shp files. Is there a way to not do that.</p>
</div>
<div id="comment-33790-info" class="comment-info">
<span class="comment-age">(08 Jun '14, 09:37)</span> <span class="comment-user userinfo">Dessus</span>
</div>
</div>
<span id="33791"></span>
<div id="comment-33791" class="comment">
<div id="post-33791-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The files I am referring to are:</p>
<p>10m-land.shp coastline-good.shp shoreline_300.shp</p>
<p>My tile server itself seems to have that data in the db without using those shape files. It seems like I am probably making this a bit harder than it needs to be ?</p>
</div>
<div id="comment-33791-info" class="comment-info">
<span class="comment-age">(08 Jun '14, 09:39)</span> <span class="comment-user userinfo">Dessus</span>
</div>
</div>
<span id="33794"></span>
<div id="comment-33794" class="comment">
<div id="post-33794-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://osmtileserver.cloudapp.net/osm/0/0/0.png">http://osmtileserver.cloudapp.net/osm/0/0/0.png</a></p>
<p>just gives a 404, suggesting that Apache doesn't know that mod_tile is supposed to be serving tiles via renderd there. As Simon says, "Please run renderd with the -f flag" and share the output via e.g. pastebin or public on Google Drive.<br />
</p>
<p>There are at least 4 sets of "how to set up a tile server" instructions on switch2osm.org, and what might be the problem will depend on which one you've followed, which will probably depend on which version of Ubuntu you're on and will determine which versions of e.g. Postgres, Mapnik etc. you're running.</p>
<p>Would it be possible to provide a few more details?</p>
<p>Also - was your new tile server working with a standard OSM style before you tried to use your OSM-Bright based one?</p>
</div>
<div id="comment-33794-info" class="comment-info">
<span class="comment-age">(08 Jun '14, 11:08)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="33795"></span>
<div id="comment-33795" class="comment">
<div id="post-33795-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have to admit that I haven't tested if newer linux versions of Mapnik actually support the Parameters section, it doesn't seemed to be used in any case. I don't think that it really makes a big difference running it on windows or not, I tend to do the former.</p>
<p>Wrt the shape files, most OSM styles use shapefiles for coast lines and other large generalised features etc. at lower zoom levels instead of retrieving them from the database. One of the reason for doing that is that coast lines break really really often and you are better off using a static version.</p>
</div>
<div id="comment-33795-info" class="comment-info">
<span class="comment-age">(08 Jun '14, 11:12)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="33796"></span>
<div id="comment-33796" class="comment">
<div id="post-33796-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The map server worked with the default style. I tried what was recommended and it seems that the following xml is causing the error here: <a href="http://pastebin.com/tGwr3gYc">http://pastebin.com/tGwr3gYc</a> with the specific error message of (forgive me for re-typing it rather than copy-paste):</p>
<p>renderd[9260]: An error occured while loading the map layer 'default': Shape Plugin: shapefile '/etc/mapnik-osm-data/C:Users\Richard\Desktop\shapedata\10m-land.shp' does not exist (encountered during parsing of layer 'land' in map '/etc/mapnik-osm-data/osm.xml</p>
</div>
<div id="comment-33796-info" class="comment-info">
<span class="comment-age">(08 Jun '14, 11:25)</span> <span class="comment-user userinfo">Dessus</span>
</div>
</div>
<span id="33798"></span>
<div id="comment-33798" class="comment not_top_scorer">
<div id="post-33798-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>(re the "c:\users\Richard..." error)</p>
<p>I'm guessing that you exported the osm.xml from within TileMill? When I've hit this sort of problem in the past I've just changed the relevant files to the correct path with a text editor. However a better option might be to export from the TileMill project via "<a href="https://github.com/mapbox/carto">carto</a>" instead (I can't find a specific citation for that though - I may have seen it via IRC; and I haven't tried to move styles from Windows to Linux for a while).</p>
</div>
<div id="comment-33798-info" class="comment-info">
<span class="comment-age">(08 Jun '14, 11:45)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="33799"></span>
<div id="comment-33799" class="comment not_top_scorer">
<div id="post-33799-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't mind using a text editor, Im just a bit confused how to translate the layers that are referencing files to the appropriate SQL query assuming that is my only issue. I have the original osm.xml and my one, but they seem quite different (and I can't find which layer in the original corresponds to the files I used (they are using different names). ie, I need:</p>
<p>Land, Coastline, and Shoreline shapes (which will be in my db, but not sure what layer/query serves them.</p>
</div>
<div id="comment-33799-info" class="comment-info">
<span class="comment-age">(08 Jun '14, 11:55)</span> <span class="comment-user userinfo">Dessus</span>
</div>
</div>
<span id="33804"></span>
<div id="comment-33804" class="comment not_top_scorer">
<div id="post-33804-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Have you tried:</p>
<p>1) Copying "10m-land.shp" to a location on your Ubuntu machine</p>
<p>2) Editing "[CDATA[C:\Users\Richard\Desktop\shapedata\10m-land.shp]]" to instead read "[CDATA[/path/to/10m-land.shp]]"</p>
<p>Apologies if I I am completely missing the point here, but that's the approach that worked for me in the past. Specifically for me it was items in TileMill's download cache that were being referenced, but this was a year or so and several TileMill versions ago and things may have changed.</p>
</div>
<div id="comment-33804-info" class="comment-info">
<span class="comment-age">(08 Jun '14, 14:56)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="33812"></span>
<div id="comment-33812" class="comment not_top_scorer">
<div id="post-33812-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I haven't tried that yet, but my point was that I should have the information in the database to do that currently (without using those files). Uploading a shp file could be a good idea for working around the problem for now (which might not be the worst idea, but doesn't seem optimal).</p>
</div>
<div id="comment-33812-info" class="comment-info">
<span class="comment-age">(08 Jun '14, 21:24)</span> <span class="comment-user userinfo">Dessus</span>
</div>
</div>
<span id="33813"></span>
<div id="comment-33813" class="comment not_top_scorer">
<div id="post-33813-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The coastlines in your database are just lines. Turning them into area's requires logic that is too complex for a stylesheet. On top of that, if you are rendering a tile too far from the coast the renderer won't even see the coastlines in the database. That is why Tilemill wants you to use the shapefiles.</p>
<p>Edit: Are the coastlines present in your database anyway? Osm2PgSQL used to leave them out by default.</p>
</div>
<div id="comment-33813-info" class="comment-info">
<span class="comment-age">(08 Jun '14, 21:36)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
</div>
<div id="comment-tools-33787" class="comment-tools">
<span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-33787-form-container" class="comment-form-container">
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

