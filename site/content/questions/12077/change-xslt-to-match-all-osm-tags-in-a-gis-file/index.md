+++
type = "question"
title = "change xslt to match all OSM tags in a GIS-file"
description = '''Hello and good day dear friends I am brandnew to GIS-Things, so please bear with me for asking a newbie question. I have an xslt that works on a split osm file[germany.osm.bz2]  i took the file called germany.osm.bz2 from this site: http://ftp5.gwdg.de/pub/misc/openstreetmap/download.geofabrik.de/ A...'''
date = "2012-04-17T09:09:00Z"
lastmod = "2012-04-18T00:18:00Z"
weight = 12077
keywords = [ "openstreetmap", "xml", "parsing", "xslt" ]
aliases = [ "/questions/12077" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [change xslt to match all OSM tags in a GIS-file](/questions/12077/change-xslt-to-match-all-osm-tags-in-a-gis-file)

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
<span id="post-12077-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12077-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12077-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello and good day dear friends</p>
<p>I am brandnew to GIS-Things, so please bear with me for asking a newbie question. I have an xslt that works on a split osm file[germany.osm.bz2]</p>
<p>i took the <strong>file called germany.osm.bz2</strong> from this site: <a href="http://ftp5.gwdg.de/pub/misc/openstreetmap/download.geofabrik.de/">http://ftp5.gwdg.de/pub/misc/openstreetmap/download.geofabrik.de/</a> Apparently, right now, i am not at home so i cannot give you a smaller piece of this large file. <strong>Note:</strong> i splitted it with XML_Split Regarding the expected output - i want to have <strong>ALL (!!)</strong> Nodes and data that are combined with the term restaurant... HTH - (End of update.)</p>
<p>I am divin into the GIS-world with a headstart: As a example i I want to do is parse all elements of <code>'amenity'</code> and <span><span><span><code>@v</code></span></span></span><code>='restaurant</code>.</p>
<p>i visited the Doku for XAPI on Openstreetmap here: <a href="http://wiki.openstreetmap.org/wiki/Xapi">http://wiki.openstreetmap.org/wiki/Xapi</a></p>
<p>Here ive found a little example to show a map with marker (with XSL Code): <a href="http://wiki.openstreetmap.org/wiki/OpenLayers_Marker">http://wiki.openstreetmap.org/wiki/OpenLayers_Marker</a></p>
<p>Note: this is only an example: i guess if i can do this with one 'amenity'` - called restaurant then i can do it with others too.</p>
<p>My <strong>first trial:</strong> What i am currently ironing out: i have a xslt-processor that runs and gives back some results..: In other words i want to gather all "available" elements (nodes, ways and relations) to match the elements I need to rework the given filter below so that we can get all elements.... See the current XSLT - and see where i stuck..</p>
<pre><code>&lt;xsl:stylesheet version = &#39;1.0&#39;
        xmlns=&quot;http://www.w3.org/1999/xhtml&quot;
        xmlns:xml_split=&quot;http://xmltwig.com/xml_split&quot;
        xmlns:xsl=&#39;http://www.w3.org/1999/XSL/Transform&#39;&gt;
&#10;    &lt;xsl:output method=&quot;text&quot; encoding=&quot;UTF-8&quot;/&gt;
    &lt;xsl:template match=&quot;/&quot;&gt;
&#10;            &lt;xsl:for-each select=&quot;xml_split:root/node/tag[@k=&#39;amenity&#39; and @v=&#39;restaurant&#39;]&quot;&gt;
            &lt;xsl:value-of select=&quot;../@id&quot;/&gt;
            &lt;xsl:text&gt;&amp;#x09;&lt;/xsl:text&gt;
            &lt;xsl:value-of select=&quot;../@lat&quot;/&gt;
            &lt;xsl:text&gt;&amp;#x09;&lt;/xsl:text&gt;
            &lt;xsl:value-of select=&quot;../@lon&quot;/&gt;
            &lt;xsl:text&gt;&amp;#x09;&lt;/xsl:text&gt;
            &lt;xsl:for-each select=&quot;../tag[@k=&#39;name&#39;]&quot;&gt;
                &lt;xsl:value-of select=&quot;@v&quot;/&gt;
            &lt;/xsl:for-each&gt;
            &lt;xsl:text&gt;&amp;#x0A;&lt;/xsl:text&gt;
        &lt;/xsl:for-each&gt;
    &lt;/xsl:template&gt;
&#10;&lt;/xsl:stylesheet&gt;</code></pre>
<p>it gives back the following results and now you see where i stuck...:</p>
<pre><code>&quot;27376049   49.6499423  8.5543447   Clubhaus SC Olympia Lorsch&quot;
&quot;27407910   49.7045590  8.5115993   Forsthaus Jägersburg&quot;
&quot;27433397   51.4588114  7.0073003   Unperfekthaus&quot;
&quot;27433643   50.0081188  9.0691993   Schützenhaus&quot;
&quot;27453754   49.6358087  8.4547972   Feldschlössel&quot;
&quot;27474067   50.1880211  9.1742722   Pizzeria A66&quot;
&quot;27475403   49.0062148  8.3369945   Marty&#39;s Restaurant&quot;
&quot;27505752   48.4081456  11.7959129  Gasthof Nagerl&quot;
&quot;27530181   49.5054702  8.7089191   Zum Pflug&quot;</code></pre>
<p>I want to have a more in depth results with all tags. What modifications do I need to make to the xslt-file?</p>
<p>I hope that I was able to ask the question correctly. If you have any questions do not hesitate to ask..</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-parsing" rel="tag" title="see questions tagged &#39;parsing&#39;">parsing</span> <span class="post-tag tag-link-xslt" rel="tag" title="see questions tagged &#39;xslt&#39;">xslt</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Apr '12, 09:09</strong></p>
<img src="https://secure.gravatar.com/avatar/600fc90e36ff81dfaba666708cf91dc5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tagtheworld&#39;s gravatar image" />
<p><span>tagtheworld</span><br />
<span class="score" title="0 reputation points">0</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tagtheworld has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12077" class="comments-container">
<span id="12078"></span>
<div id="comment-12078" class="comment">
<div id="post-12078-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Sorry for the off-topic but... Do you really need to use xslt ?</p>
<p>I imagine in this forum you'll find more people able to help if you use one of osm's many parsing libraries (or even a standard xml parsing library) and a for_loop in the language of your choice rather than xslt (which is a rather unpopular technology).</p>
</div>
<div id="comment-12078-info" class="comment-info">
<span class="comment-age">(17 Apr '12, 11:14)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="12080"></span>
<div id="comment-12080" class="comment">
<div id="post-12080-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hi vincent - thx for the quick help. I am pretty new to xslt and also new to xml too. but i am willing to learn - if any body can help me it would be a great pleasure to dive into another technology..</p>
</div>
<div id="comment-12080-info" class="comment-info">
<span class="comment-age">(17 Apr '12, 11:31)</span> <span class="comment-user userinfo">tagtheworld</span>
</div>
</div>
<span id="12084"></span>
<div id="comment-12084" class="comment">
<div id="post-12084-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>To add a little more to what Vincent de P said - some XML documents are governed by strict rules as to the values that they can contain. OSM isn't really like that - there's even a wiki document expaining that you can with caveats use <a href="http://wiki.openstreetmap.org/wiki/Any_tags_you_like">any tags you like</a>.</p>
<p>What might help a little is if you could explain a bit about what you're trying to do with the data. It may be that there's an existing service (such as the <a href="http://wiki.openstreetmap.org/wiki/Xapi">XAPI</a> that allows you to get at what you want rather than starting with flat XML), or it may be that you need to put the OSM data in a database optimised for the task that you want to perform (for rendering map tiles for example, there are instructions <a href="http://switch2osm.org/serving-tiles/">here</a>).</p>
<p>The problem is that alongside the name there are manu, many other tags that might get used alongside amenity=restaurant (see <a href="http://taginfo.openstreetmap.org/tags/amenity=restaurant#combinations">here</a> for a list). Also, have a look at the "See Also" section of the amenity=restaurant <a href="http://wiki.openstreetmap.org/wiki/Restaurant">wiki page</a> for this that an establishment might get tagged as other than "restaurant".</p>
</div>
<div id="comment-12084-info" class="comment-info">
<span class="comment-age">(17 Apr '12, 13:32)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="12098"></span>
<div id="comment-12098" class="comment">
<div id="post-12098-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hello dear SomeoneElse hello dear Vincent de p</p>
<p>many thanks for the answers and the hints. Great to see such support to a newbie i want to play with the data - and see how i can transform data fom one formate to another. Well if it is easy to work with XAPI or other methods - well ithougth that it would be pretty eays to enlarge the xslt to a enriched version - that covers some more entities - eg. the adress of the restaurant and some more stuff. Well i want to see how i can move the data into a database!`? Any idea or help greatly appreciated</p>
</div>
<div id="comment-12098-info" class="comment-info">
<span class="comment-age">(17 Apr '12, 21:00)</span> <span class="comment-user userinfo">tagtheworld</span>
</div>
</div>
<span id="12102"></span>
<div id="comment-12102" class="comment">
<div id="post-12102-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>can i do some requests on POIs of Openstreetmap with XAPI.</p>
<p>doing like so: i send a request to the API-Server - over http</p>
<p>as a respond i get the following result - in XML</p>
<p>example: the following link gives back all the Nodes of the Type amenity=restaurant in XML-Format. the bounding box (bbox) limits the area:</p>
<p><a href="http://xapi.openstreetmap.org/api/0.6/node%5Bamenity=restaurant%5D%5Bbbox=9.4908142,48.7810801,9.5660019,48.8387351%5D">http://xapi.openstreetmap.org/api/0.6/node[amenity=restaurant][bbox=9.4908142,48.7810801,9.5660019,48.8387351]</a></p>
<p>well i get a blank page back - this is making me wondering...</p>
</div>
<div id="comment-12102-info" class="comment-info">
<span class="comment-age">(17 Apr '12, 22:56)</span> <span class="comment-user userinfo">tagtheworld</span>
</div>
</div>
<span id="12106"></span>
<div id="comment-12106" class="comment not_top_scorer">
<div id="post-12106-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>... which continues into <a href="http://help.openstreetmap.org/questions/12100/xapi-request-runs-into-server-error-how-can-make-sense-of-xapi">this question</a> about the XAPI specificallly.</p>
</div>
<div id="comment-12106-info" class="comment-info">
<span class="comment-age">(18 Apr '12, 00:18)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-12077" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-12077-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

