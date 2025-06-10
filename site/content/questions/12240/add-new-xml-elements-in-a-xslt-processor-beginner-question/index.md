+++
type = "question"
title = "Add new xml-elements in a xslt-processor [beginner-question]"
description = '''hello and good day dear xml-friends,  i am new to xml so do not bear with me for the questions... i am currently making some tests with an xslt-processor -  new: see the update i added at this initial-posting - for a solution i i copy the logic for the tag name... -&amp;gt; i added an example at the end...'''
date = "2012-04-21T15:53:00Z"
lastmod = "2012-04-21T15:53:00Z"
weight = 12240
keywords = [ "xml", "openstreetmap", "xslt" ]
aliases = [ "/questions/12240" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Add new xml-elements in a xslt-processor \[beginner-question\]](/questions/12240/add-new-xml-elements-in-a-xslt-processor-beginner-question)

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
<span id="post-12240-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12240-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12240-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hello and good day dear xml-friends,</p>
<p>i am new to xml so do not bear with me for the questions... i am currently making some tests with an xslt-processor -</p>
<p><strong>new:</strong> see the <strong>update</strong> i added at this initial-posting - for a solution i i copy the logic for the tag name... -&gt; i added an example at the end of the initial-posting. plz lemme know your idas...thgx</p>
<p><strong>new:</strong> see the <strong>update</strong> i added at this initial-posting - for a solution i i copy the logic for the tag name... -&gt; i added an example at the end of the initial-posting. plz lemme know your idas...thgx</p>
<pre><code>&lt;xsl:stylesheet version = &#39;1.0&#39;
    xmlns=&quot;http://www.w3.org/1999/xhtml&quot;
    xmlns:xsl=&#39;http://www.w3.org/1999/XSL/Transform&#39;&gt;
&#10;    &lt;xsl:output method=&quot;text&quot; encoding=&quot;UTF-8&quot;/&gt;
    &lt;xsl:template match=&quot;/&quot;&gt;
&#10;        &lt;xsl:for-each select=&quot;/osm/node/tag[@k=&#39;amenity&#39; and @v=&#39;restaurant&#39;]&quot;&gt;
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
&lt;xsl:for-each select=&quot;../tag[@k=&#39;website&#39;]&quot;&gt;
    &lt;xsl:value-of select=&quot;@v&quot;/&gt;
    &lt;/xsl:for-each&gt;
    &lt;xsl:text&gt;&amp;#x0A;&lt;/xsl:text&gt;
    &lt;/xsl:template&gt;
&lt;/xsl:stylesheet&gt;</code></pre>
<p><strong>Note:</strong> this above mentioned solution does not give any iadditional infos - so the website is <strong>NOT shown</strong>. what is wrong here!?</p>
<p>here the initial posting starts.</p>
<p>i run this on terminal to parse the xml-document</p>
<p><strong>Question:</strong> what i want is to enlarge the xslt-processor with the following tags</p>
<pre><code>wheelchair
website    
addr:country
addr:street
addr:city
addr:housenumber</code></pre>
<ul>
<li><p>see more details in a example here ...:</p>
<p>&lt;tag k="addr:postcode" v="73614"/&gt; &lt;tag k="wheelchair" v="yes"/&gt; &lt;tag k="website" v="www.kesselhaus-schorndorf.de"/&gt; &lt;tag k="addr:country" v="DE"/&gt; &lt;tag k="name" v="Kesselhaus"/&gt; &lt;tag k="amenity" v="restaurant"/&gt; &lt;tag k="addr:street" v="Arnoldstraße"/&gt; &lt;tag k="addr:city" v="Schorndorf"/&gt; &lt;tag k="addr:housenumber" v="3"/&gt;</p></li>
</ul>
<p>i run the following code: time xsltproc test3.xslt testdoc3.xml &gt; restaurants-004.csv</p>
<pre><code>&lt;xsl:stylesheet version = &#39;1.0&#39;
    xmlns=&quot;http://www.w3.org/1999/xhtml&quot;
    xmlns:xsl=&#39;http://www.w3.org/1999/XSL/Transform&#39;&gt;
&#10;    &lt;xsl:output method=&quot;text&quot; encoding=&quot;UTF-8&quot;/&gt;
    &lt;xsl:template match=&quot;/&quot;&gt;
&#10;        &lt;xsl:for-each select=&quot;/osm/node/tag[@k=&#39;amenity&#39; and @v=&#39;restaurant&#39;]&quot;&gt;
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
&lt;/xsl:stylesheet&gt;</code></pre>
<p>....on <strong>this xml-document</strong> - which is called <strong>testdoc3.xml</strong></p>
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
<p>i get back these results - and yes: i want to enlarge it with the above mentioned tags...</p>
<pre><code>185612117   48.8037523  9.5248779   Courage
252619189   48.8067032  9.5314986   Kesselhaus
319597380   48.8277913  9.5477029   Gasthaus zur Linde
319597382   48.8282523  9.5503109   China-Garden
339591124   48.7888015  9.5079525   Pizzeria da Rocco
392682646   48.8315734  9.5468864   Gasthaus an der Wieslauf
454516720   48.8031264  9.5344371   Deutsches Haus
572362430   48.807953   9.5379673   Club Kneipe
613988559   48.7991827  9.551828    Gaststätte Schützenhaus
631421882   48.8070643  9.5437351   Remstalstuben
672817732   48.8045127  9.5254423   Hanti Alem
677555759   48.8048108  9.5243952   Weinstube St. Urban
677578941   48.8052132  9.5246951   Bei Domenico
677578944   48.8055998  9.5261987   Little Saigon</code></pre>
<p>again the wanted tags that enlarge the xslt-preprocessor are the following ones...</p>
<pre><code>wheelchair
website    
addr:country
addr:street
addr:city
addr:housenumber</code></pre>
<p>thx for any and all help - thx in advance</p>
<p>greetigngs</p>
<p><strong>update</strong>- i do it liek so - in copying the logic <strong>for the tag name</strong> - eg to add the tag <strong>for website:</strong></p>
<pre><code>&lt;xsl:for-each select=&quot;../tag[@k=&#39;website&#39;]&quot;&gt;
    &lt;xsl:value-of select=&quot;@v&quot;/&gt;
    &lt;/xsl:for-each&gt;
    &lt;xsl:text&gt;&amp;#x0A;&lt;/xsl:text&gt;
&lt;/xsl:for-each&gt;</code></pre>
<p><strong>what you say!?</strong></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-xslt" rel="tag" title="see questions tagged &#39;xslt&#39;">xslt</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Apr '12, 15:53</strong></p>
<img src="https://secure.gravatar.com/avatar/600fc90e36ff81dfaba666708cf91dc5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tagtheworld&#39;s gravatar image" />
<p><span>tagtheworld</span><br />
<span class="score" title="0 reputation points">0</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tagtheworld has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Apr '12, 16:40</strong> </span></p>
</div>
</div>
<div id="comments-container-12240" class="comments-container">
&#10;</div>
<div id="comment-tools-12240" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12240-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

