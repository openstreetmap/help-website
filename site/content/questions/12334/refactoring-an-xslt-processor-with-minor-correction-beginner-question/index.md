+++
type = "question"
title = "refactoring an XSLT processor with minor correction [beginner-question]"
description = '''i have a extremely large xml-file - which is derived from the field of geo informatics. i got it from a German subsite or the OpenStreetMap-Project: the Geograpical-Engineering-site that deilvers a weekly snapshot of OpenStreetMap of a certain area: i took the germany.osm.bz2 from here http://ftp5.g...'''
date = "2012-04-24T16:33:00Z"
lastmod = "2012-04-24T20:41:00Z"
weight = 12334
keywords = [ "openstreetmap", "xml", "xslt", "mysql" ]
aliases = [ "/questions/12334" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [refactoring an XSLT processor with minor correction \[beginner-question\]](/questions/12334/refactoring-an-xslt-processor-with-minor-correction-beginner-question)

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
<span id="post-12334-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12334-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12334-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>i have a extremely large xml-file - which is derived from the field of geo informatics. i got it from a German subsite or the OpenStreetMap-Project: the Geograpical-Engineering-site that deilvers a weekly snapshot of OpenStreetMap of a certain area: i took the germany.osm.bz2 from here <a href="http://ftp5.gwdg.de/pub/misc/openstreetmap/download.geofabrik.de/">http://ftp5.gwdg.de/pub/misc/openstreetmap/download.geofabrik.de/</a></p>
<p>For doing some tests with xslt i want to run a request to find out certain entity - let us take for example the restaurants. we want to find out all the restaurants in the area.</p>
<p>now we can run that directly on the bz2 compressed file, that we downloaded - for example if we use the following code:</p>
<pre><code>bzcat germany.osm.bz2 | xsltproc restaurants.xslt - &gt; restaurants,csv</code></pre>
<p>well i splitted the file with xml_split -which is a great perl-module from CPAN.</p>
<p><strong>The problem:</strong> with the following xslt-processor i get only bad results - the parsed files werent not parsed enough i only get a minor set of informations when i run the code on a xml-file. see the xslt-processor - and below - a litte data-chunk out of the file i run and parse if you want to check it - just get the little dataset - note it is a splitted file</p>
<p>here you can get it: <a href="https://rapidshare.com/#!download%7C643p12%7C2523227518%7Cgermany-001.xml%7C100000">https://rapidshare.com/#!download|643p12|2523227518|germany-001.xml|100000</a></p>
<p>Note: see therefore the important lines: <code>xmlns:xml_split="http://xmltwig.com/xml_split"</code> and this one here:</p>
<pre><code> &lt;xsl:for-each select=&quot;xml_split:root/node/tag[@k=&#39;amenity&#39; and @v=&#39;restaurant&#39;]&quot;&gt;</code></pre>
<p><strong>Note</strong>- you can run a little test - and see how long it takes to parse time xsltproc restaurants.xslt germany-001.xml &gt; restaurants-001.csv</p>
<pre><code>real    0m0.308s
user    0m0.283s
sys     0m0.022s</code></pre>
<p>here we have the xslt-processor that contains the code for parsing...:</p>
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
        &lt;xsl:value-of select=&quot;./tag[@k = &#39;cuisine&#39;]/@v&quot;/&gt;
        &lt;xsl:text&gt;&amp;#x09;&lt;/xsl:text&gt;
        &lt;xsl:value-of select=&quot;./tag[@k = &#39;wheelchair&#39;]/@v&quot;/&gt;
        &lt;xsl:text&gt;&amp;#x09;&lt;/xsl:text&gt;
        &lt;xsl:value-of select=&quot;./tag[@k = &#39;website&#39;]/@v&quot;/&gt;
        &lt;xsl:text&gt;&amp;#x09;&lt;/xsl:text&gt;
        &lt;xsl:value-of select=&quot;./tag[@k = &#39;addr:country&#39;]/@v&quot;/&gt;
        &lt;xsl:text&gt;&amp;#x09;&lt;/xsl:text&gt;
        &lt;xsl:value-of select=&quot;./tag[@k = &#39;addr:city&#39;]/@v&quot;/&gt;
        &lt;xsl:text&gt;&amp;#x09;&lt;/xsl:text&gt;        
        &lt;xsl:value-of select=&quot;./tag[@k = &#39;addr:street&#39;]/@v&quot;/&gt;
        &lt;xsl:text&gt;&amp;#x09;&lt;/xsl:text&gt;
        &lt;xsl:value-of select=&quot;./tag[@k = &#39;addr:housenumber&#39;]/@v&quot;/&gt;
        &lt;xsl:text&gt;&amp;#x0A;&lt;/xsl:text&gt;
    &lt;/xsl:for-each&gt;
    &lt;/xsl:template&gt;
&#10;&lt;/xsl:stylesheet&gt;</code></pre>
<p>and here below we have a data-chunk out of the xml-file that we have parsed: see it</p>
<pre><code>&lt;node id=&quot;52768810&quot; lat=&quot;48.2044749&quot; lon=&quot;11.3249434&quot; version=&quot;7&quot; changeset=&quot;9490517&quot; user=&quot;wheelmap_visitor&quot; uid=&quot;290680&quot; timestamp=&quot;2011-10-07T20:24:46Z&quot;&gt;
    &lt;tag k=&quot;addr:city&quot; v=&quot;Olching&quot; /&gt;
    &lt;tag k=&quot;addr:country&quot; v=&quot;DE&quot; /&gt;
    &lt;tag k=&quot;addr:housenumber&quot; v=&quot;72&quot; /&gt;
    &lt;tag k=&quot;addr:postcode&quot; v=&quot;82140&quot; /&gt;
    &lt;tag k=&quot;addr:street&quot; v=&quot;Hauptstraße&quot; /&gt;
    &lt;tag k=&quot;amenity&quot; v=&quot;restaurant&quot; /&gt;
    &lt;tag k=&quot;cuisine&quot; v=&quot;mexican&quot; /&gt;
    &lt;tag k=&quot;email&quot; v=&quot;info@cantina-olching.de&quot; /&gt;
    &lt;tag k=&quot;name&quot; v=&quot;La Cantina&quot; /&gt;
    &lt;tag k=&quot;opening_hours&quot; v=&quot;Mo-Su 17:00-01:00&quot; /&gt;
    &lt;tag k=&quot;phone&quot; v=&quot;+49 (8142) 444393&quot; /&gt;
    &lt;tag k=&quot;website&quot; v=&quot;http://www.cantina-olching.com/&quot; /&gt;
    &lt;tag k=&quot;wheelchair&quot; v=&quot;no&quot; /&gt;
&lt;/node&gt;</code></pre>
<p>see the results - note there are missing some parts - unfortunatly..</p>
<pre><code>51923772    49.0812534  8.5637183   Zur Talschänke
&#10;52040576    49.4635433  12.4287292  Emil-Kemmer-Haus
&#10;52141326    49.4144243  12.4143153  Gasthaus Plecher
&#10;52623232    48.9293634  8.2722549   Korfu
&#10;52664989    49.0435133  8.3919370   Restaurant Zentrum
&#10;52754898    49.3243828  12.3618662  Gasthaus Irlbacher
&#10;52762875    49.0099641  8.2528132   Langasthof Stober
&#10;52765672    50.0082768  9.2139632   Wirtshaus im Frohnrad
&#10;52768810    48.2044749  11.3249434  La Cantina
&#10;52768816    48.2051698  11.3257964  Indian Palace
&#10;52768826    48.2073264  11.3276147  Dorfstub&#39;n
&#10;52768830    48.2075968  11.3281055  Le Candele
&#10;52774284    49.0319471  8.2888353   Zum Anker</code></pre>
<p>well it is somewhat a problem that i get the results - ive tried alot but at the moment i am glueless why i get the little output - that is totally contrary to the tags i have in the xslt -processor - any idea and hint will be greatly appreciatdd</p>
<p>btw: after all i want to run approx 5000 files that are the result of the split - and subsequently i want to collect all the results in a mysql-database...</p>
<p>here you can get the <strong>original-file:</strong> <a href="http://ftp5.gwdg.de/pub/misc/openstreetmap/download.geofabrik.de">http://ftp5.gwdg.de/pub/misc/openstreetmap/download.geofabrik.de</a> ( germany.osm.bz2 01-Apr-2012 14:51 1.7G )</p>
<p>and here a <strong>splitted one:</strong> <a href="https://rapidshare.com/#!download%7C643p12%7C2523227518%7Cgermany-001.xml%7C100000">https://rapidshare.com/#!download|643p12|2523227518|germany-001.xml|100000</a></p>
<p>i have to refactor the coed -so the question - is - how can i get the mysql-results on a efficient way?</p>
<p><strong>update:</strong>thx to the first answer in this thread i startet to refactor the code - but still lack of some better results. i have to retry it again..lots of changes were suggested - i did a quick walktrough on the xslt-parser: with the first trial of refactoring i got some funny results. But i will try again - i go trough all the xslt-processor-code and have a closer look if i find the errors and finally i try to refactor all the xslt-file. - any pointers and subbestions or code-snippets are greatly wellcome.</p>
<p>Well to me it looks like our <code>./tag[</code><span><span><span><span><span><span><span><span><span><span><span><span><span><span><code>@k</code></span></span></span></span></span></span></span></span></span></span></span></span></span></span><code> = '???']/</code><span><span><span><span><span><span><span><span><span><span><span><span><span><code>@v</code></span></span></span></span></span></span></span></span></span></span></span></span></span> xpath should be somewhat <code>../tag[</code><span><span><span><span><span><span><span><span><span><span><span><span><span><span><code>@k</code></span></span></span></span></span></span></span></span></span></span></span></span></span></span><code>='???']</code>, because our context node is our original matching <code>tag</code> element, not the <code>node</code> element.</p>
<p>we should consider somewhat changing the context node to make this code clearer and avoid errors like this:</p>
<pre><code>&lt;xsl:for-each select=&quot;xml_split:root/node[tag[@k=&#39;amenity&#39; and @v=&#39;restaurant&#39;]]&quot;&gt;</code></pre>
<p>Then we can use XPaths like select="tag/<span><span>@id</span></span>"<code>and</code>tag[<span><span><span><span><span><span><span><span><span><span><span><span><span><span>@k</span></span></span></span></span></span></span></span></span></span></span></span></span></span>='country']/<span><span><span><span><span><span><span><span><span><span><span><span><span>@v</span></span></span></span></span></span></span></span></span></span></span></span></span>`.</p>
<p>But above all we should consider refactoring this code to make better use of <code>template</code> instead of <code>for-each</code>.</p>
<p>what do you think - any pointer towards the refactoring is grealy appreciated</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-xslt" rel="tag" title="see questions tagged &#39;xslt&#39;">xslt</span> <span class="post-tag tag-link-mysql" rel="tag" title="see questions tagged &#39;mysql&#39;">mysql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Apr '12, 16:33</strong></p>
<img src="https://secure.gravatar.com/avatar/600fc90e36ff81dfaba666708cf91dc5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tagtheworld&#39;s gravatar image" />
<p><span>tagtheworld</span><br />
<span class="score" title="0 reputation points">0</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tagtheworld has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Apr '12, 16:33</strong> </span></p>
</div>
</div>
<div id="comments-container-12334" class="comments-container">
&#10;</div>
<div id="comment-tools-12334" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12334-form-container" class="comment-form-container">
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

<span id="12337"></span>

<div id="answer-container-12337" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12337-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12337-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-12337-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is not an XSLT help desk. Your problem is not related to OSM except that you use OSM test data; it would probably be better to discuss these things in a forum dedicated to XML processing in general.</p>
<p>You write that eventually you want the data in a MySQL database. Is there any reason why you don't just bin the whole XSLT stuff and import the data into MySQL using Osmosis or something like <a href="https://github.com/skyebook/OSMGenerator?">https://github.com/skyebook/OSMGenerator?</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Apr '12, 19:49</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-12337" class="comments-container">
<span id="12338"></span>
<div id="comment-12338" class="comment">
<div id="post-12338-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hello frederik thx for the answer - well it would be very interesting to import the whole stuff into a mysql-db. at which stage can we do a import into mysql!? At a very early stage of the data-processing,,,,</p>
</div>
<div id="comment-12338-info" class="comment-info">
<span class="comment-age">(24 Apr '12, 20:21)</span> <span class="comment-user userinfo">tagtheworld</span>
</div>
</div>
<span id="12339"></span>
<div id="comment-12339" class="comment">
<div id="post-12339-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hello after a quick look at the options of importing i muse bout the db-shemes. Is it possible to do certain requests on the data - if they are imported into mysql - i heard about the problem of consistency and such issues . i will dig deeper into the issues - come back and report all the findings. greeting</p>
</div>
<div id="comment-12339-info" class="comment-info">
<span class="comment-age">(24 Apr '12, 20:41)</span> <span class="comment-user userinfo">tagtheworld</span>
</div>
</div>
</div>
<div id="comment-tools-12337" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12337-form-container" class="comment-form-container">
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

