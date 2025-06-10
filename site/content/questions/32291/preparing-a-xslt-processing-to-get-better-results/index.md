+++
type = "question"
title = "preparing a xslt-processing  to  get better results"
description = '''on opensuse 13.1 i try to do some gis-works with a large file: france-latest.osm.bz2 which i gathered from here: [url]http://download.geofabrik.de/europe.html[/url] what do i do with that file france-latest.osm.bz2  bzcat france-latest.osm.bz2  what is aimed? i want to extract all things that belong...'''
date = "2014-04-11T11:38:00Z"
lastmod = "2014-04-12T21:43:00Z"
weight = 32291
keywords = [ "extract" ]
aliases = [ "/questions/32291" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [preparing a xslt-processing to get better results](/questions/32291/preparing-a-xslt-processing-to-get-better-results)

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
<span id="post-32291-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32291-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32291-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>on opensuse 13.1 i try to do some gis-works with a large file: france-latest.osm.bz2 which i gathered from here: [url]<a href="http://download.geofabrik.de/europe.html%5B/url%5D">http://download.geofabrik.de/europe.html[/url]</a></p>
<p>what do i do with that file france-latest.osm.bz2</p>
<pre><code>   bzcat france-latest.osm.bz2</code></pre>
<p>what is aimed? i want to extract all things that belong to the POI restaurant which is long lat name adress etc - etx.</p>
<p>i have the following things up and running:</p>
<p>package perl-XML-Twig and run xml_split</p>
<p>with a command available on openSUSE to split xml files named xml_split (it is part of the package perl-XML-Twig) Now we try to run the following command (I hope we have enough hard disk space since the output is roughly 20GB).</p>
<pre><code> bzcat france.osm.bz2 | xml_split -s 100M -b france -n 3 -</code></pre>
<p>this will result in a bunch of 100 Mb large xml files france-001.xml,france-002.xml and so on. Weu then have the xslt (the name of the root element) and of course we will need a loop in the bash to process the several files and collect all the results together.</p>
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
<p>question: what do i need to get all the aimed data out of the dataset - i.e.</p>
<p>long lat name adress etc - etx.</p>
<p>here below we have a data-chunk out of the xml-file that we have parsed: see it</p>
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
    &lt;tag k=&quot;wheelchair&quot; v=&quot;no&quot; /&gt;</code></pre>
<p>well - how to get all the data out of the above mentioned file with the xslt-processing</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Apr '14, 11:38</strong></p>
<img src="https://secure.gravatar.com/avatar/bf4d2d8660e82c4a7387b7d2a8a8cfcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="say_hello_to_the_world&#39;s gravatar image" />
<p><span>say_hello_to...</span><br />
<span class="score" title="19 reputation points">19</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="say_hello_to_the_world has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Apr '14, 11:41</strong> </span></p>
</div>
</div>
<div id="comments-container-32291" class="comments-container">
<span id="32306"></span>
<div id="comment-32306" class="comment">
<div id="post-32306-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I would NOT recommend using xslt to extract data from OSM XML files. It's just a lot more work and more complicated than using some of the available OSM tools.</p>
</div>
<div id="comment-32306-info" class="comment-info">
<span class="comment-age">(11 Apr '14, 15:39)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="32316"></span>
<div id="comment-32316" class="comment">
<div id="post-32316-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hello dear sk53 many many thanks - i will follow your advices and will do as you recommend. btw - if i have a big big file such as the one of germany - should i separate it into pieces using xml-split!?</p>
</div>
<div id="comment-32316-info" class="comment-info">
<span class="comment-age">(12 Apr '14, 13:39)</span> <span class="comment-user userinfo">say_hello_to...</span>
</div>
</div>
<span id="32320"></span>
<div id="comment-32320" class="comment">
<div id="post-32320-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Personally, I'd use <a href="http://wiki.openstreetmap.org/wiki/Osmosis">osmosis</a> to extract data from within a large downloaded .osm or osm.pbf file</p>
</div>
<div id="comment-32320-info" class="comment-info">
<span class="comment-age">(12 Apr '14, 14:16)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="32322"></span>
<div id="comment-32322" class="comment">
<div id="post-32322-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>See also <a href="http://forum.openstreetmap.org/viewtopic.php?id=25031">this forum question</a> which seems to be related (and has a bit more info).</p>
</div>
<div id="comment-32322-info" class="comment-info">
<span class="comment-age">(12 Apr '14, 15:48)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-32291" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32291-form-container" class="comment-form-container">
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

<span id="32323"></span>

<div id="answer-container-32323" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32323-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32323-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-32323-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="say_hello_to_the_world has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I wouldn't get hung up on the fact that OSM data's in XML format. As <span>@SK53</span> suggested above, there are lots of existing OSM tools for extracting data (most of which have had questions asked about before here).<br />
</p>
<p>I'd extract (an initially small) geographical area using <a href="https://help.openstreetmap.org/search/?q=osmosis&amp;Submit=Search&amp;t=question">osmosis</a>, then look at using <a href="https://help.openstreetmap.org/search/?q=osmfilter&amp;Submit=Search&amp;t=question">osmfilter</a> to extract the data (possibly having used <a href="https://help.openstreetmap.org/search/?q=osmconvert&amp;Submit=Search&amp;t=question">osmconvert</a> to convert the data into a format that osmfilter can understand). Also perhaps consider <a href="https://help.openstreetmap.org/search/?q=osmium&amp;Submit=Search&amp;t=question">osmium</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '14, 15:56</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span> </br></p>
</div>
</div>
<div id="comments-container-32323" class="comments-container">
<span id="32330"></span>
<div id="comment-32330" class="comment">
<div id="post-32330-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>many many thanks for all your ideas - i will add all those packages on opensuse 13.1 .- hopefully i will get them installed - either via commandline or yast</p>
</div>
<div id="comment-32330-info" class="comment-info">
<span class="comment-age">(12 Apr '14, 21:07)</span> <span class="comment-user userinfo">say_hello_to...</span>
</div>
</div>
</div>
<div id="comment-tools-32323" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32323-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="32292"></span>

<div id="answer-container-32292" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32292-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32292-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32292-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Are you aware that bzcat and bz2 file name extension is a hint to a compressed osm file?</p>
<p>You have to uncompress it in the very right way, so I would NOT recommend to use anything like a pipe in your console prompt.</p>
<p>Instead of downloading france.osm.bz2 ... try the osm.pbf file ... it is a kind of binary format.</p>
<p>Then you should get familiar with the tools calles osmconvert and osmfilter ... see the OSM wiki how to use them.</p>
<p>and before processing the whole France, I recommend to try some tests before with a smaller country extract or a region extract available also via geofabrik.de</p>
<p>With osmconvert you can produce a CSV file from raw OSM data, to load in a database or spreadsheet programm.</p>
<p>Success?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Apr '14, 12:12</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-32292" class="comments-container">
<span id="32310"></span>
<div id="comment-32310" class="comment">
<div id="post-32310-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>He already uncompresses it via <code>bzcat</code>.</p>
</div>
<div id="comment-32310-info" class="comment-info">
<span class="comment-age">(11 Apr '14, 21:23)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="32314"></span>
<div id="comment-32314" class="comment">
<div id="post-32314-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hello dear stephan many many thanks - i will follow your advices and will do as you recommend.</p>
<p>i try to work on a smaller country-extract or region - guess that geofabrik has some.</p>
<p>love to do some conversions to csv - or to load into a db-or spreadsheet</p>
</div>
<div id="comment-32314-info" class="comment-info">
<span class="comment-age">(12 Apr '14, 13:37)</span> <span class="comment-user userinfo">say_hello_to...</span>
</div>
</div>
<span id="32317"></span>
<div id="comment-32317" class="comment">
<div id="post-32317-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>btw - if i have a big big file such as the one of germany - should i separate it into pieces using xml-split!?</p>
</div>
<div id="comment-32317-info" class="comment-info">
<span class="comment-age">(12 Apr '14, 13:39)</span> <span class="comment-user userinfo">say_hello_to...</span>
</div>
</div>
</div>
<div id="comment-tools-32292" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32292-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="32333"></span>

<div id="answer-container-32333" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32333-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32333-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32333-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>btw - i also installed osmfilter: see here</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Osmfilter">http://wiki.openstreetmap.org/wiki/Osmfilter</a></p>
<pre><code>Download and build in one run:   wget -O - http://m.m.i24.cc/osmfilter.c |cc -x c - -O3 -o osmfilter
&#10;As usual: There is no warranty, to the extent permitted by law.
&#10;linux-70ce:/home/martin #  wget -O - http://m.m.i24.cc/osmfilter.c |cc -x c - -O3 -o osmfilter
--2014-04-12 22:34:49--  http://m.m.i24.cc/osmfilter.c
Auflösen des Hostnamen »m.m.i24.cc (m.m.i24.cc)«... 80.67.17.148, 2a00:1158:0:300:432f::1
Verbindungsaufbau zu m.m.i24.cc (m.m.i24.cc)|80.67.17.148|:80... verbunden.
HTTP-Anforderung gesendet, warte auf Antwort... 200 OK
Länge: 213497 (208K) [text/plain]
In »»STDOUT«« speichern.
&#10;100%[==========================================================================================================================================&gt;] 213.497     1,14MB/s   in 0,2s
&#10;2014-04-12 22:34:49 (1,14 MB/s) - auf die Standardausgabe geschrieben [213497/213497]
&#10;&lt;stdin&gt;: In function ‘oo__close’:
&lt;stdin&gt;:5166:5: warning: call to function ‘read_close’ without a real prototype [-Wunprototyped-calls]
&lt;stdin&gt;:1079:13: note: ‘read_close’ was declared here
linux-70ce:/home/martin #</code></pre>
<p>i am not sure if it succeedet or failed!?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '14, 21:43</strong></p>
<img src="https://secure.gravatar.com/avatar/bf4d2d8660e82c4a7387b7d2a8a8cfcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="say_hello_to_the_world&#39;s gravatar image" />
<p><span>say_hello_to...</span><br />
<span class="score" title="19 reputation points">19</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="say_hello_to_the_world has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-32333" class="comments-container">
&#10;</div>
<div id="comment-tools-32333" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32333-form-container" class="comment-form-container">
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

