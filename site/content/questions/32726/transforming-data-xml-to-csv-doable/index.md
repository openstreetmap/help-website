+++
type = "question"
title = "transforming data xml to csv: doable?"
description = '''i am pretty new to openstreetmap update see below! we can run Perl for text-mangling XML-Simple-2.20/lib/XML/Simple.pm here&#x27;s an example of a little script to parse our XML: #!/usr/bin/perl use strict; use warnings; use XML::Simple; use Data::Dumper;  my $xmlfile = shift || die &quot;Usage: $0 &amp;lt;XML_FI...'''
date = "2014-04-28T21:09:00Z"
lastmod = "2014-11-08T11:50:00Z"
weight = 32726
keywords = [ "xml", "overpass", "csv" ]
aliases = [ "/questions/32726" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [transforming data xml to csv: doable?](/questions/32726/transforming-data-xml-to-csv-doable)

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
<span id="post-32726-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32726-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32726-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>i am pretty new to openstreetmap</p>
<p><strong>update see below!</strong></p>
<p>we can run Perl for text-mangling XML-Simple-2.20/lib/XML/Simple.pm here's an example of a little script to parse our XML:</p>
<pre><code>#!/usr/bin/perl
use strict;
use warnings;
use XML::Simple;
use Data::Dumper;
&#10;my $xmlfile = shift || die &quot;Usage: $0 &lt;XML_FILE&gt;\n&quot;;
&#10;my $ref;
eval {
  $ref = XMLin($xmlfile,
    ForceArray    =&gt; 0,
    KeyAttr       =&gt; [ ],
    SuppressEmpty =&gt; &#39;&#39;,
  ) or die &quot;Can&#39;t read XML from $xmlfile: $!\n&quot;;
};
die $@ if($@);
print Dumper $ref;</code></pre>
<p>which, if passed our XML file goes very well</p>
<p>on <a href="http://overpass-turbo.eu/">http://overpass-turbo.eu/</a> i have runned the following code</p>
<p>i run the following code in opverpass-api - see here <a href="http://overpass-turbo.eu/">http://overpass-turbo.eu/</a></p>
<pre><code>&lt;query type=&quot;node&quot;&gt;
  &lt;has-kv k=&quot;place&quot; v=&quot;city&quot;/&gt;
  &lt;has-kv k=&quot;name&quot; v=&quot;Peking&quot;/&gt;
&lt;/query&gt;
&lt;query type=&quot;node&quot;&gt;
  &lt;around radius=&quot;1000&quot;/&gt;
    &lt;has-kv k=&quot;shop&quot;/&gt;
&lt;/query&gt;
&lt;print/&gt;</code></pre>
<p>Export of the data to the following formats</p>
<pre><code>to GeoJSON
to GPX
to KML</code></pre>
<p>get the data from</p>
<p>see the Overpass API-explanations: i have the options to loat them to JOSM laden (only for requests, that give back valid OSM-XML with Metadata) GeoJSON to save it as gist</p>
<p>note - i did not install the overpass-api on my opensuse 13.1 yet. but i am willing to do so.</p>
<p>as for now - running the above mentioned code in the oerpass-api - here. <a href="http://overpass-turbo.eu/">http://overpass-turbo.eu/</a></p>
<p>how to treat it to get it exported as csv-formated hope i was able to provide all the necessary things for a clear and concise question.</p>
<p>all i want is to transforme the xml-data to csv - in order to get a excel or calc based output.</p>
<pre><code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;osm version=&quot;0.6&quot; generator=&quot;Overpass API&quot;&gt;
&lt;note&gt;The data included in this document is from www.openstreetmap.org. The data is made available under ODbL.&lt;/note&gt;
&lt;meta osm_base=&quot;2014-04-27T13:49:02Z&quot;/&gt;
&#10;  &lt;node id=&quot;297489767&quot; lat=&quot;49.4085014&quot; lon=&quot;8.6941465&quot;&gt;
    &lt;tag k=&quot;addr:city&quot; v=&quot;Heidelberg&quot;/&gt;
    &lt;tag k=&quot;addr:housenumber&quot; v=&quot;23&quot;/&gt;
    &lt;tag k=&quot;addr:postcode&quot; v=&quot;69115&quot;/&gt;
    &lt;tag k=&quot;addr:street&quot; v=&quot;Sofienstraße&quot;/&gt;
    &lt;tag k=&quot;name&quot; v=&quot;ARLT&quot;/&gt;
    &lt;tag k=&quot;phone&quot; v=&quot;+49 6221 20229&quot;/&gt;
    &lt;tag k=&quot;shop&quot; v=&quot;computer&quot;/&gt;
    &lt;tag k=&quot;source&quot; v=&quot;survey&quot;/&gt;
    &lt;tag k=&quot;website&quot; v=&quot;http://www.arlt.com&quot;/&gt;
    &lt;tag k=&quot;wheelchair&quot; v=&quot;yes&quot;/&gt;
  &lt;/node&gt;
  &lt;node id=&quot;305144906&quot; lat=&quot;49.4060012&quot; lon=&quot;8.6929652&quot;&gt;
    &lt;tag k=&quot;addr:city&quot; v=&quot;Heidelberg&quot;/&gt;
    &lt;tag k=&quot;addr:country&quot; v=&quot;DE&quot;/&gt;
    &lt;tag k=&quot;addr:housenumber&quot; v=&quot;13-15&quot;/&gt;
    &lt;tag k=&quot;addr:postcode&quot; v=&quot;69115&quot;/&gt;
    &lt;tag k=&quot;addr:state&quot; v=&quot;Baden-Württemberg&quot;/&gt;
    &lt;tag k=&quot;addr:street&quot; v=&quot;Rohrbacher Straße&quot;/&gt;
    &lt;tag k=&quot;name&quot; v=&quot;Heidel-bike&quot;/&gt;
    &lt;tag k=&quot;opening_hours&quot; v=&quot;Tu-Fr 10:00-18:30; Sa 10:00-14:00&quot;/&gt;
    &lt;tag k=&quot;shop&quot; v=&quot;bicycle&quot;/&gt;
    &lt;tag k=&quot;website&quot; v=&quot;http://www.heidelbike.de/&quot;/&gt;
    &lt;tag k=&quot;wheelchair&quot; v=&quot;yes&quot;/&gt;
  &lt;/node&gt;
  &lt;node id=&quot;305963167&quot; lat=&quot;49.4139877&quot; lon=&quot;8.6924247&quot;&gt;
    &lt;tag k=&quot;addr:city&quot; v=&quot;Heidelberg&quot;/&gt;
    &lt;tag k=&quot;addr:country&quot; v=&quot;DE&quot;/&gt;
    &lt;tag k=&quot;addr:housenumber&quot; v=&quot;4&quot;/&gt;
    &lt;tag k=&quot;addr:postcode&quot; v=&quot;69120&quot;/&gt;
    &lt;tag k=&quot;addr:street&quot; v=&quot;Brückenstraße&quot;/&gt;
    &lt;tag k=&quot;name&quot; v=&quot;Buchhandlung Schmitt &amp;amp; Hahn&quot;/&gt;
    &lt;tag k=&quot;shop&quot; v=&quot;books&quot;/&gt;
    &lt;tag k=&quot;wheelchair&quot; v=&quot;no&quot;/&gt;</code></pre>
<p>look forward to hear from you</p>
<p><strong>update</strong> found this interesting thing: <a href="http://stackoverflow.com/questions/5491056/how-to-import-xml-file-into-mysql-database-table-using-xml-load-function">http://stackoverflow.com/questions/5491056/how-to-import-xml-file-into-mysql-database-table-using-xml-load-function</a></p>
<p>have an XML file which looks like this :</p>
<pre><code>    &lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&#10;&lt;resultset statement=&quot;YOUR SQL STATEMENTS TO GENERATE THIS XML FILE&quot; xmlns:xsi=&quot;http://www.w3.org/2001/XMLSchema-instance&quot;&gt;
  &lt;row&gt;
    &lt;field name=&quot;personal_number&quot;&gt;539&lt;/field&gt;
    &lt;field name=&quot;firstname&quot;&gt;Name&lt;/field&gt;
    &lt;field name=&quot;lastname&quot;&gt;Surname&lt;/field&gt;
    &lt;field name=&quot;email&quot;&gt;email.domain.com&lt;/field&gt;
    &lt;field name=&quot;start_time&quot;&gt;2011-04-02 13:30:00&lt;/field&gt;
    &lt;field name=&quot;end_time&quot;&gt;2011-04-02 18:15:00&lt;/field&gt;
    &lt;field name=&quot;employee_category&quot;&gt;1,2,4,5,22,37,38,39,41,43,44&lt;/field&gt;
  &lt;/row&gt;
  &lt;row&gt;
    &lt;field name=&quot;personal_number&quot;&gt;539&lt;/field&gt;
    &lt;field name=&quot;firstname&quot;&gt;Name&lt;/field&gt;
    &lt;field name=&quot;lastname&quot;&gt;Surname&lt;/field&gt;
    &lt;field name=&quot;email&quot;&gt;email.domain.com&lt;/field&gt;
    &lt;field name=&quot;start_time&quot;&gt;2011-04-02 13:30:00&lt;/field&gt;
    &lt;field name=&quot;end_time&quot;&gt;2011-04-02 18:15:00&lt;/field&gt;
    &lt;field name=&quot;employee_category&quot;&gt;1,2,4,5,22,37,38,39,41,43,44&lt;/field&gt;
  &lt;/row&gt;
  &lt;row&gt;
    &lt;field name=&quot;personal_number&quot;&gt;539&lt;/field&gt;
    &lt;field name=&quot;firstname&quot;&gt;Name&lt;/field&gt;
    &lt;field name=&quot;lastname&quot;&gt;Surname&lt;/field&gt;
    &lt;field name=&quot;email&quot;&gt;email.domain.com&lt;/field&gt;
    &lt;field name=&quot;start_time&quot;&gt;2011-04-02 13:30:00&lt;/field&gt;
    &lt;field name=&quot;end_time&quot;&gt;2011-04-02 18:15:00&lt;/field&gt;
    &lt;field name=&quot;employee_category&quot;&gt;1,2,4,5,22,37,38,39,41,43,44&lt;/field&gt;
  &lt;/row&gt;</code></pre>
<p>I am trying to import it in MySQL using SQL statement :</p>
<pre><code>use databasename;
LOAD XML LOCAL INFILE &#39;/pathtofile/file.xml&#39; INTO TABLE my_tablename;</code></pre>
<p>The table my_tablename has the following fields :</p>
<pre><code>id (auto increment id)
personal_number(varchar)
firstname(varchar) 
lastname(varchar)
email(varchar) 
start_time(varchar)
end_time(varchar)
employee_category(varchar)</code></pre>
<p>I get error : Error Code: 1136 Column count doesn't match value count at row 1</p>
<p>I am using MySQL 5.1.56</p>
<p>I assume this error occurs because the database table has field id, which is not present in the XML file. How is it possible to import this XML file using MySQL queries of built in functions such that it skips id column during the import and relies on the auto increment function for the id column? Is there some smarter way of handling XML file imports im MySQL? Maybe there is better statement which allows to specify column mapping?</p>
<p>we can specify fields like this:</p>
<pre><code>LOAD XML LOCAL INFILE &#39;/pathtofile/file.xml&#39; 
INTO TABLE my_tablename(personal_number, firstname, ...);</code></pre>
<p>since ID is auto increment, you can also specify ID=NULL as,</p>
<pre><code>LOAD XML LOCAL INFILE &#39;/pathtofile/file.xml&#39; INTO TABLE my_tablename SET ID=NULL;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Apr '14, 21:09</strong></p>
<img src="https://secure.gravatar.com/avatar/bf4d2d8660e82c4a7387b7d2a8a8cfcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="say_hello_to_the_world&#39;s gravatar image" />
<p><span>say_hello_to...</span><br />
<span class="score" title="19 reputation points">19</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="say_hello_to_the_world has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Apr '14, 10:33</strong> </span></p>
</div>
</div>
<div id="comments-container-32726" class="comments-container">
<span id="32739"></span>
<div id="comment-32739" class="comment">
<div id="post-32739-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Please edit your question to make it easier to read for everybody and that supporters don't need to walk trough dozens of lines. 1. What is your problem? 2. What did you tried? 3. Where do you fail?</p>
</div>
<div id="comment-32739-info" class="comment-info">
<span class="comment-age">(29 Apr '14, 11:42)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
</div>
<div id="comment-tools-32726" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32726-form-container" class="comment-form-container">
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

<span id="38375"></span>

<div id="answer-container-38375" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38375-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38375-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-38375-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Overpass API v0.7.51 now comes with native CSV support, so you don't need to download an extract from Geofabrik and post-process that extract using <code>osmconvert</code> anymore:</p>
<p>Here's an example for Overpass turbo which returns all pharmacies in Lüneburg along with their OSM id, lat, lon, name, operator, etc.</p>
<pre><code>[out:csv(::id, ::lat, ::lon,  amenity, name, operator, opening_hours, &quot;contact:website&quot;, &quot;contact:phone&quot;, brand, dispensing, lastcheck)];
&#10;{{geocodeArea:Lüneburg}}-&gt;.searchArea;
&#10;(
  node[&quot;amenity&quot;=&quot;pharmacy&quot;](area.searchArea);
  way[&quot;amenity&quot;=&quot;pharmacy&quot;](area.searchArea);
  relation[&quot;amenity&quot;=&quot;pharmacy&quot;](area.searchArea);
);
out center;</code></pre>
<p>Example: <a href="http://overpass-turbo.eu/s/5Qc">http://overpass-turbo.eu/s/5Qc</a></p>
<p>If you click on "Export" -&gt; "raw data directly from Overpass API" you can even directly load OSM data into LibreOffice/Excel. Data is separated by a "tab" character by default and comes with a header line (can be adjusted).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Nov '14, 11:50</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
</div>
<div id="comments-container-38375" class="comments-container">
&#10;</div>
<div id="comment-tools-38375" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38375-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="32747"></span>

<div id="answer-container-32747" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32747-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32747-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-32747-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please type CSV in the text searchbox of this FAQ site, and you will get some hints how you can convert raw OSM data to CSV data.</p>
<p>And please avoid to do crosspostings in OSM forum and here at the same time. Thanks.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Apr '14, 16:21</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-32747" class="comments-container">
&#10;</div>
<div id="comment-tools-32747" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32747-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="32763"></span>

<div id="answer-container-32763" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32763-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32763-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-32763-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Possibly the simplest way to convert OSM data to CSV is using osmconvert: <a href="http://wiki.openstreetmap.org/wiki/Osmconvert">http://wiki.openstreetmap.org/wiki/Osmconvert</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Apr '14, 11:39</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-32763" class="comments-container">
&#10;</div>
<div id="comment-tools-32763" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32763-form-container" class="comment-form-container">
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

