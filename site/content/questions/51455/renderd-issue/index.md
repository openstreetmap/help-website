+++
type = "question"
title = "Renderd issue"
description = '''Hi, i follow the tutorial in https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/ When i do the command renderd -f -c /usr/local/etc/renderd.conf and send me this error renderd[78029]: An error ocurred while loading the map layer &#x27;default&#x27;: Shape Plugin: shapefile  &#x27;/usr/local...'''
date = "2016-08-16T19:58:00Z"
lastmod = "2016-11-25T06:40:00Z"
weight = 51455
keywords = [ "renderd" ]
aliases = [ "/questions/51455" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Renderd issue](/questions/51455/renderd-issue)

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
<span id="post-51455-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51455-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51455-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, i follow the tutorial in <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/</a></p>
<p>When i do the command</p>
<p>renderd -f -c /usr/local/etc/renderd.conf</p>
<p>and send me this error</p>
<p>renderd[78029]: An error ocurred while loading the map layer 'default': Shape Plugin: shapefile '/usr/local/share/maps/style/osm-bright-master/shp/ne_10m_populated_places/ne_10m_populated_places.shp' does not exist encountered during parsing of layer 'ne_places' in Layer at line 45546 of '/usr/local/share/maps/style/OSMBright/OSMBright.xml'</p>
<p>Some hint to resolve this issue?</p>
<p>Regards</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Aug '16, 19:58</strong></p>
<img src="https://secure.gravatar.com/avatar/edb5c98eae6e9e9a22cea03ce01bac7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HugoLaraS1979&#39;s gravatar image" />
<p><span>HugoLaraS1979</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HugoLaraS1979 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-51455" class="comments-container">
<span id="51460"></span>
<div id="comment-51460" class="comment">
<div id="post-51460-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Does the file "ne_10m_populated_places.shp" exist in that location?</p>
</div>
<div id="comment-51460-info" class="comment-info">
<span class="comment-age">(16 Aug '16, 22:33)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-51455" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51455-form-container" class="comment-form-container">
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

<span id="51461"></span>

<div id="answer-container-51461" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51461-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51461-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51461-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I believe that what's happened is that the the "ne populated places" source has changed and the OSMBright script (which is Mapbox's) hasn't been updated to match it.</p>
<p>The last time I set up OSMBright was to answer <a href="http://help.openstreetmap.org/questions/50435/duplicate-town-names/50447">this</a> question, and do vaguely remember having to extract some shapefiles manually and move them around. I also did have to fiddle about with the <a href="https://github.com/SomeoneElseOSM/openstreetmap-carto-AJT/commits/master/get-shapefiles.sh">script</a> that I do use that does the same job. You should be able to figure out the data location from that, and manually move the shapefiles that you need to the right place. It's not ideal, but it should get you a working stylesheet.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Aug '16, 22:41</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Aug '16, 22:44</strong> </span></p>
</div>
</div>
<div id="comments-container-51461" class="comments-container">
&#10;</div>
<div id="comment-tools-51461" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51461-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="51456"></span>

<div id="answer-container-51456" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51456-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51456-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51456-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The line 45546 of OSMBright.xml is</p>
<p>&lt;layer name="ne_places" srs="+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs"&gt;</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Aug '16, 20:00</strong></p>
<img src="https://secure.gravatar.com/avatar/edb5c98eae6e9e9a22cea03ce01bac7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HugoLaraS1979&#39;s gravatar image" />
<p><span>HugoLaraS1979</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HugoLaraS1979 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Aug '16, 20:01</strong> </span></p>
</div>
</div>
<div id="comments-container-51456" class="comments-container">
<span id="51458"></span>
<div id="comment-51458" class="comment">
<div id="post-51458-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>is this an answer to your problem or just a clarification of your question?</p>
</div>
<div id="comment-51458-info" class="comment-info">
<span class="comment-age">(16 Aug '16, 21:48)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="51464"></span>
<div id="comment-51464" class="comment">
<div id="post-51464-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For completeness, that's a reference to the layer name which references the file that isn't in the right place yet. That's why its saying error "at line 45546". The main useful bit of information is what you've said in the question:</p>
<p>'/usr/local/share/maps/style/osm-bright-master/shp/ne_10m_populated_places/ne_10m_populated_places.shp' does not exist</p>
</div>
<div id="comment-51464-info" class="comment-info">
<span class="comment-age">(16 Aug '16, 22:52)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-51456" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51456-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53105"></span>

<div id="answer-container-53105" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53105-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53105-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53105-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As I was just testing my tile server I commented this lines to be able to run the tile server:</p>
<pre><code>&lt;Layer name=&quot;ne_places&quot;srs=&quot;+proj=longlat +ellps=WGS84 +datum=WGS84+no_defs&quot;&gt;                                                                                                                                                            
                                                                                                                                                                                                                    &lt;Datasource&gt;                                                                                                                                                                                                     
   &lt;Parameter name=&quot;dbname&quot;&gt;&lt;![CDATA[osm]]&gt;&lt;Parameter&gt;                                                                                                                                                          
   &lt;Parameter name=&quot;extent&quot;&gt;&lt;![CDATA[-20037508.34 -20037508.34 20037508.34 20037508.34]]&gt;&lt;Parameter&gt;                                                                                                            
   &lt;Parameter name=&quot;file&quot;&gt;&lt;![CDATA[/usr/local/share/maps/style/osm-bright-master/shp/ne_10m_populated_places/ne_10m_populated_places.shp]]&gt;&lt;Parameter&gt;                                                          
   &lt;Parameter name=&quot;srs&quot;&gt;&lt;![CDATA[+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0.0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs +over]]&gt;&lt;Parameter&gt;                                
   &lt;Parameter name=&quot;type&quot;&gt;&lt;![CDATA[shape]]&gt;&lt;Parameter&gt;                                                                                                                                                          
&lt;Datasource&gt;                                                                                          &lt;Layer&gt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Nov '16, 06:40</strong></p>
<img src="https://secure.gravatar.com/avatar/6863bef08c5e0bc17bee1e10c2b56b83?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Potdeyaourt&#39;s gravatar image" />
<p><span>Potdeyaourt</span><br />
<span class="score" title="61 reputation points">61</span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Potdeyaourt has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Nov '16, 06:41</strong> </span></p>
</div>
</div>
<div id="comments-container-53105" class="comments-container">
&#10;</div>
<div id="comment-tools-53105" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53105-form-container" class="comment-form-container">
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

