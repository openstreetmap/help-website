+++
type = "question"
title = "xslt-processor gives back top-results on one dataset and no results on another"
description = '''hello and good day dear xml-friends,  i am new to xml so do not bear with me for the questions... i am currently making some tests with an xslt-processor -  I ve got an script that runs nicely on one test-dataset - and gives back good and valid results and contrary to this behaviour i get back silly...'''
date = "2012-04-22T08:02:00Z"
lastmod = "2012-04-22T08:02:00Z"
weight = 12253
keywords = [ "xml", "openstreetmap", "mysql" ]
aliases = [ "/questions/12253" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [xslt-processor gives back top-results on one dataset and no results on another](/questions/12253/xslt-processor-gives-back-top-results-on-one-dataset-and-no-results-on-another)

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
<span id="post-12253-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12253-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12253-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hello and good day dear xml-friends,</p>
<p>i am new to xml so do not bear with me for the questions... i am currently making some tests with an xslt-processor - I ve got an script that runs nicely on one test-dataset - and gives back good and valid results and contrary to this behaviour i get back silly and dumb results if i run the same script - note: i get back a csv-formatted file with 2 MB that contains only tabstops... funny but true...</p>
<p>so here my script is:</p>
<p>if i run this xslt-code on the following test-dataset i get only bad bad results - only tabstops... nothing more... what causes this errors. note - i get better results if i run the code againgst the second dataset .- see far below... and see the results at the end of this inital posting....</p>
<pre><code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;
&lt;xsl:stylesheet version=&quot;1.0&quot; xmlns:xsl=&quot;http://www.w3.org/1999/XSL/Transform&quot;&gt;
&#10;    &lt;xsl:output method=&quot;text&quot; encoding=&quot;utf-8&quot; /&gt;
&#10;    &lt;xsl:template match=&quot;/&quot;&gt;
        &lt;xsl:apply-templates /&gt;
    &lt;/xsl:template&gt;
&#10;    &lt;xsl:template match=&quot;osm&quot;&gt;
        &lt;xsl:apply-templates /&gt;
    &lt;/xsl:template&gt;
&#10;    &lt;xsl:template match=&quot;node[tag[@k=&#39;amenity&#39; and @v=&#39;restaurant&#39;]]&quot;&gt;
        &lt;xsl:value-of select=&quot;./@id&quot;/&gt;
        &lt;xsl:text&gt;&amp;#x09;&lt;/xsl:text&gt;
        &lt;xsl:value-of select=&quot;./@lat&quot;/&gt;
        &lt;xsl:text&gt;&amp;#x09;&lt;/xsl:text&gt;
        &lt;xsl:value-of select=&quot;./@lon&quot;/&gt;
        &lt;xsl:text&gt;&amp;#x09;&lt;/xsl:text&gt;
        &lt;xsl:value-of select=&quot;./tag[@k = &#39;cuisine&#39;]/@v&quot;/&gt;
        &lt;xsl:text&gt;&amp;#x09;&lt;/xsl:text&gt;
        &lt;xsl:value-of select=&quot;./tag[@k = &#39;name&#39;]/@v&quot;/&gt;
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
    &lt;/xsl:template&gt;
        &lt;!-- all non-restaurant nodes --&gt;
    &lt;xsl:template match=&quot;node[tag[@k=&#39;amenity&#39; and @v!=&#39;restaurant&#39;]]&quot; /&gt;
&#10;&lt;/xsl:stylesheet&gt;</code></pre>
<p>if i run this against this test-dataset - then i get only dumb results a file with only tabstops in. i have no glue what causes the error?</p>
&lt;xml_split:root xmlns:xml_split="http://xmltwig.com/xml_split"&gt;
<pre><code>&lt;node id=&quot;25242198&quot; lat=&quot;49.0077605&quot; lon=&quot;8.3560676&quot; version=&quot;9&quot; changeset=&quot;10151199&quot; user=&quot;keinname&quot; uid=&quot;165061&quot; timestamp=&quot;2011-12-18T22:59:43Z&quot;&gt;
    &lt;tag k=&quot;addr:city&quot; v=&quot;Karlsruhe&quot; /&gt;
    &lt;tag k=&quot;addr:country&quot; v=&quot;DE&quot; /&gt;
    &lt;tag k=&quot;addr:housenumber&quot; v=&quot;6&quot; /&gt;
    &lt;tag k=&quot;addr:postcode&quot; v=&quot;76185&quot; /&gt;
    &lt;tag k=&quot;addr:street&quot; v=&quot;Durmersheimer Straße&quot; /&gt;
    &lt;tag k=&quot;amenity&quot; v=&quot;restaurant&quot; /&gt;
    &lt;tag k=&quot;beer_garden&quot; v=&quot;yes&quot; /&gt;
    &lt;tag k=&quot;cuisine&quot; v=&quot;german&quot; /&gt;
    &lt;tag k=&quot;name&quot; v=&quot;Beim Schupi&quot; /&gt;
    &lt;tag k=&quot;opening_hours&quot; v=&quot;Mo-Sa 17:00+; Su 12:00+&quot; /&gt;
    &lt;tag k=&quot;phone&quot; v=&quot;+49 721 551220&quot; /&gt;
    &lt;tag k=&quot;website&quot; v=&quot;http://www.schupi.de&quot; /&gt;
&lt;/node&gt;</code></pre>
<p>[...]...</p>
<p>Note: i get back silly and bad results - only tabstops and nothing more..</p>
<p>but if if i run the above mentioned xslt-processor-code on the following xml-dataset i get back good results... see below - !!!</p>
<pre><code>&lt;?xml version=&#39;1.0&#39; encoding=&#39;UTF-8&#39;?&gt;
&lt;osm version=&quot;0.6&quot; generator=&quot;Osmosis SNAPSHOT-r26564&quot;&gt;
  &lt;node id=&quot;185612117&quot; version=&quot;5&quot; timestamp=&quot;2011-01-08T19:23:43Z&quot; uid=&quot;290680&quot; user=&quot;wheelmap_visitor&quot; changeset=&quot;6906586&quot; lat=&quot;48.8037523&quot; lon=&quot;9.5248779&quot;&gt;
    &lt;tag k=&quot;addr:postcode&quot; v=&quot;73614&quot;/&gt;
    &lt;tag k=&quot;wheelchair&quot; v=&quot;yes&quot;/&gt;
    &lt;tag k=&quot;website&quot; v=&quot;http://www.courage-restaurant.de/&quot;/&gt;
    &lt;tag k=&quot;addr:country&quot; v=&quot;DE&quot;/&gt;
    &lt;tag k=&quot;name&quot; v=&quot;Courage&quot;/&gt;
    &lt;tag k=&quot;amenity&quot; v=&quot;restaurant&quot;/&gt;
    &lt;tag k=&quot;addr:street&quot; v=&quot;Künkelinstraße&quot;/&gt;
    &lt;tag k=&quot;addr:city&quot; v=&quot;Schorndorf&quot;/&gt;
    &lt;tag k=&quot;addr:housenumber&quot; v=&quot;33&quot;/&gt;
  &lt;/node&gt;
  &lt;node id=&quot;252619189&quot; version=&quot;5&quot; timestamp=&quot;2011-01-08T19:21:43Z&quot; uid=&quot;290680&quot; user=&quot;wheelmap_visitor&quot; changeset=&quot;6906586&quot; lat=&quot;48.8067032&quot; lon=&quot;9.5314986&quot;&gt;
    &lt;tag k=&quot;addr:postcode&quot; v=&quot;73614&quot;/&gt;
    &lt;tag k=&quot;wheelchair&quot; v=&quot;yes&quot;/&gt;
    &lt;tag k=&quot;website&quot; v=&quot;www.kesselhaus-schorndorf.de&quot;/&gt;
    &lt;tag k=&quot;addr:country&quot; v=&quot;DE&quot;/&gt;
    &lt;tag k=&quot;name&quot; v=&quot;Kesselhaus&quot;/&gt;
    &lt;tag k=&quot;amenity&quot; v=&quot;restaurant&quot;/&gt;
    &lt;tag k=&quot;addr:street&quot; v=&quot;Arnoldstraße&quot;/&gt;
    &lt;tag k=&quot;addr:city&quot; v=&quot;Schorndorf&quot;/&gt;
    &lt;tag k=&quot;addr:housenumber&quot; v=&quot;3&quot;/&gt;
  &lt;/node&gt;
  &lt;node id=&quot;319597380&quot; version=&quot;1&quot; timestamp=&quot;2008-12-17T21:13:15Z&quot; changeset=&quot;444629&quot; lat=&quot;48.8277913&quot; lon=&quot;9.5477029&quot;&gt;
    &lt;tag k=&quot;name&quot; v=&quot;Gasthaus zur Linde&quot;/&gt;
    &lt;tag k=&quot;amenity&quot; v=&quot;restaurant&quot;/&gt;
  &lt;/node&gt;
  &lt;node id=&quot;319597382&quot; version=&quot;1&quot; timestamp=&quot;2008-12-17T21:13:15Z&quot; changeset=&quot;444629&quot; lat=&quot;48.8282523&quot; lon=&quot;9.5503109&quot;&gt;
    &lt;tag k=&quot;name&quot; v=&quot;China-Garden&quot;/&gt;
    &lt;tag k=&quot;amenity&quot; v=&quot;restaurant&quot;/&gt;
  &lt;/node&gt;
  &lt;node id=&quot;339591124&quot; version=&quot;2&quot; timestamp=&quot;2011-09-22T17:33:36Z&quot; uid=&quot;290680&quot; user=&quot;wheelmap_visitor&quot; changeset=&quot;9366746&quot; lat=&quot;48.7888015&quot; lon=&quot;9.5079525&quot;&gt;
    &lt;tag k=&quot;cuisine&quot; v=&quot;italian&quot;/&gt;
    &lt;tag k=&quot;wheelchair&quot; v=&quot;limited&quot;/&gt;
    &lt;tag k=&quot;name&quot; v=&quot;Pizzeria da Rocco&quot;/&gt;
    &lt;tag k=&quot;amenity&quot; v=&quot;restaurant&quot;/&gt;
  &lt;/node&gt;
  &lt;node id=&quot;392682646&quot; version=&quot;3&quot; timestamp=&quot;2010-05-11T19:00:20Z&quot; uid=&quot;12973&quot; user=&quot;MattGPS&quot; changeset=&quot;4671372&quot; lat=&quot;48.8315734&quot; lon=&quot;9.5468864&quot;&gt;
    &lt;tag k=&quot;name&quot; v=&quot;Gasthaus an der Wieslauf&quot;/&gt;
    &lt;tag k=&quot;amenity&quot; v=&quot;restaurant&quot;/&gt;
  &lt;/node&gt;
  &lt;node id=&quot;454516720&quot; version=&quot;4&quot; timestamp=&quot;2010-12-11T15:30:21Z&quot; uid=&quot;12982&quot; user=&quot;Michael Schulze&quot; changeset=&quot;6625571&quot; lat=&quot;48.8031264&quot; lon=&quot;9.5344371&quot;&gt;
    &lt;tag k=&quot;addr:postcode&quot; v=&quot;73614&quot;/&gt;
    &lt;tag k=&quot;cuisine&quot; v=&quot;regional&quot;/&gt;
    &lt;tag k=&quot;website&quot; v=&quot;http://www.deutscheshaus-schorndorf.de/&quot;/&gt;
    &lt;tag k=&quot;addr:country&quot; v=&quot;DE&quot;/&gt;
    &lt;tag k=&quot;name&quot; v=&quot;Deutsches Haus&quot;/&gt;
    &lt;tag k=&quot;amenity&quot; v=&quot;restaurant&quot;/&gt;
    &lt;tag k=&quot;addr:street&quot; v=&quot;Sonnenscheinstraße&quot;/&gt;
    &lt;tag k=&quot;addr:city&quot; v=&quot;Schorndorf&quot;/&gt;
    &lt;tag k=&quot;addr:housenumber&quot; v=&quot;13&quot;/&gt;
  &lt;/node&gt;
  &lt;node id=&quot;572362430&quot; version=&quot;3&quot; timestamp=&quot;2010-07-04T06:59:50Z&quot; uid=&quot;106522&quot; user=&quot;neuntoeter&quot; changeset=&quot;5130101&quot; lat=&quot;48.807953&quot; lon=&quot;9.5379673&quot;&gt;
    &lt;tag k=&quot;smoking&quot; v=&quot;no&quot;/&gt;
    &lt;tag k=&quot;name&quot; v=&quot;Club Kneipe&quot;/&gt;
    &lt;tag k=&quot;amenity&quot; v=&quot;restaurant&quot;/&gt;
  &lt;/node&gt;
  &lt;node id=&quot;613988559&quot; version=&quot;1&quot; timestamp=&quot;2010-01-15T01:20:03Z&quot; uid=&quot;24748&quot; user=&quot;mabapla&quot; changeset=&quot;3621550&quot; lat=&quot;48.7991827&quot; lon=&quot;9.551828&quot;&gt;
    &lt;tag k=&quot;name&quot; v=&quot;Gaststätte Schützenhaus&quot;/&gt;
    &lt;tag k=&quot;amenity&quot; v=&quot;restaurant&quot;/&gt;
  &lt;/node&gt;
  &lt;node id=&quot;859532091&quot; version=&quot;1&quot; timestamp=&quot;2010-08-13T23:05:14Z&quot; uid=&quot;130472&quot; user=&quot;fx99&quot; changeset=&quot;5486736&quot; lat=&quot;48.8062337&quot; lon=&quot;9.5278548&quot;&gt;
    &lt;tag k=&quot;website&quot; v=&quot;http://www.weinstube-buechsenmacher.de/&quot;/&gt;
    &lt;tag k=&quot;name&quot; v=&quot;Weinstube zum Büchsenmacher&quot;/&gt;
    &lt;tag k=&quot;amenity&quot; v=&quot;restaurant&quot;/&gt;
    &lt;tag k=&quot;addr:housename&quot; v=&quot;5&quot;/&gt;
    &lt;tag k=&quot;addr:street&quot; v=&quot;Höllgasse&quot;/&gt;
  &lt;/node&gt;
  &lt;node id=&quot;1625565012&quot; version=&quot;1&quot; timestamp=&quot;2012-02-09T18:00:04Z&quot; uid=&quot;131968&quot; user=&quot;changchun_1&quot; changeset=&quot;10636279&quot; lat=&quot;48.8151893&quot; lon=&quot;9.5310692&quot;&gt;
    &lt;tag k=&quot;name&quot; v=&quot;Gasthaus Sonne&quot;/&gt;
    &lt;tag k=&quot;amenity&quot; v=&quot;restaurant&quot;/&gt;
  &lt;/node&gt;
&lt;/osm&gt;</code></pre>
<p>see the -fairly good !! - results i get when i run the xslt-processor on the second dataset: i have no glue why i get such nasty results - when i apply the xslt-processor on the first dataset...!?</p>
<pre><code>185612117   48.8037523  9.5248779       Courage yes http://www.courage-restaurant.de/   DE  Schorndorf  Künkelinstraße  33
&#10;252619189   48.8067032  9.5314986       Kesselhaus  yes www.kesselhaus-schorndorf.de    DE  Schorndorf  Arnoldstraße    3
&#10;319597380   48.8277913  9.5477029       Gasthaus zur Linde
&#10;319597382   48.8282523  9.5503109       China-Garden
&#10;339591124   48.7888015  9.5079525   italian Pizzeria da Rocco   limited
&#10;392682646   48.8315734  9.5468864       Gasthaus an der Wieslauf
&#10;454516720   48.8031264  9.5344371   regional    Deutsches Haus      http://www.deutscheshaus-schorndorf.de/ DE  Schorndorf  Sonnenscheinstraße  13</code></pre>
<p>any idea and pointer towards a solution is greatly wellcome... thx in advance!!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-mysql" rel="tag" title="see questions tagged &#39;mysql&#39;">mysql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Apr '12, 08:02</strong></p>
<img src="https://secure.gravatar.com/avatar/600fc90e36ff81dfaba666708cf91dc5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tagtheworld&#39;s gravatar image" />
<p><span>tagtheworld</span><br />
<span class="score" title="0 reputation points">0</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tagtheworld has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12253" class="comments-container">
&#10;</div>
<div id="comment-tools-12253" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12253-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

