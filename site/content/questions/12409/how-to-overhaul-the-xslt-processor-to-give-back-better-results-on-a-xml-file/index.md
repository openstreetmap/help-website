+++
type = "question"
title = "[closed] how to overhaul the xslt-processor to give back better results on a xml-file?"
description = '''For doing some tests with xslt i want to run a request to find out certain entity - let us take for example the restaurants. we want to find out all the restaurants in the area. now we can run that directly on the bz2 compressed file, that we downloaded - for example if we use the following code: bz...'''
date = "2012-04-28T18:24:00Z"
lastmod = "2012-04-28T19:27:00Z"
weight = 12409
keywords = [ "xml", "xslt" ]
aliases = [ "/questions/12409" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] how to overhaul the xslt-processor to give back better results on a xml-file?](/questions/12409/how-to-overhaul-the-xslt-processor-to-give-back-better-results-on-a-xml-file)

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
<span id="post-12409-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12409-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12409-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>For doing some tests with xslt i want to run a request to find out certain entity - let us take for example the restaurants. we want to find out all the restaurants in the area.</p>
<p>now we can run that directly on the bz2 compressed file, that we downloaded - for example if we use the following code:</p>
<pre><code>bzcat germany.osm.bz2 | xsltproc restaurants.xslt - &gt; restaurants,csv</code></pre>
<p>well i splitted the file with xml_split -which is a great perl-module from CPAN.</p>
<p><strong>The problem:</strong> with the following xslt-processor i get only bad results - the parsed files werent not parsed enough i only get a minor set of informations when i run the code on a xml-file. see the xslt-processor - and below - a litte data-chunk out of the file i run and parse if you want to check it - just get the little dataset - note it is a splitted file</p>
<p>here you can get it: <a href="https://rapidshare.com/#!download%7C643p12%7C2523227518%7Cgermany-001.xml%7C100000">https://rapidshare.com/#!download|643p12|2523227518|germany-001.xml|100000</a></p>
<p><strong>Note:</strong> see therefore the important lines: <code>xmlns:xml_split="http://xmltwig.com/xml_split"</code>and this one here:</p>
<p><strong>Note:</strong> here we have a much more little-file which is very very small - compared with the one that is mentioned above. <a href="https://rapidshare.com/files/2447253717/germany-081.xml">https://rapidshare.com/files/2447253717/germany-081.xml</a> Here we have the xslt-processor that has difficulties with gathering theinformation - the xslt-procssor should be reengineerd a bit. well i tried seferal things ... but at the moment i got stuck some how...:</p>
<p>Some musings regarding the overhaul of the code: well at least it looks like the code needs an overhaul. hmmm - i should consider changing the code to make it clearer and avoid errors. Well above all: i think i should make useage of XPaths like select="tag/<span><span>@id</span></span>" and tag[<span><span><span><span><span><span><span><span><span><span><span>@k</span></span></span></span></span></span></span></span></span></span></span>='country']/<span><span><span><span><span><span><span><span><span><span><span>@v</span></span></span></span></span></span></span></span></span></span></span>. But above all - i really think that i should consider refactoring this code to make better use of template. What do you think..</p>
<p>Below i show you the code that runs against the two files - mainly against this one here: <a href="https://rapidshare.com/files/2447253717/germany-081.xml">https://rapidshare.com/files/2447253717/germany-081.xml</a></p>
&lt;xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
<pre><code>&lt;xsl:output method=&quot;text&quot; encoding=&quot;utf-8&quot; /&gt;
&lt;xsl:template match=&quot;/&quot;&gt;
    &lt;xsl:apply-templates /&gt;
&lt;/xsl:template&gt;
&lt;xsl:template match=&quot;osm&quot;&gt;
    &lt;xsl:apply-templates /&gt;
&lt;/xsl:template&gt;
&lt;xsl:template match=&quot;node[tag[@k=&#39;amenity&#39; and @v=&#39;restaurant&#39;]]&quot;&gt;
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
&#10;&lt;!-- all non-restaurant nodes --&gt;
&lt;xsl:template match=&quot;node[tag[@k=&#39;amenity&#39; and @v!=&#39;restaurant&#39;]]&quot; /&gt;</code></pre>
&lt;/xsl:stylesheet&gt;
<p>how to rework the xslt in order to work smooothly?</p>
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
<p>see the results - note there are missing some parts - unfortunatly.. <strong>Question:</strong> How can we rearrange and reengineer the code so that it procudes better results on the above mentioned files:</p>
<p>By the way:here you can get it:</p>
<p><a href="https://rapidshare.com/#!download%7C643p12%7C2523227518%7Cgermany-001.xml%7C100000">https://rapidshare.com/#!download|643p12|2523227518|germany-001.xml|100000</a></p>
<p><a href="https://rapidshare.com/files/2447253717/germany-081.xml">https://rapidshare.com/files/2447253717/germany-081.xml</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-xslt" rel="tag" title="see questions tagged &#39;xslt&#39;">xslt</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Apr '12, 18:24</strong></p>
<img src="https://secure.gravatar.com/avatar/600fc90e36ff81dfaba666708cf91dc5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tagtheworld&#39;s gravatar image" />
<p><span>tagtheworld</span><br />
<span class="score" title="0 reputation points">0</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tagtheworld has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>28 Apr '12, 19:44</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-12409" class="comments-container">
<span id="12410"></span>
<div id="comment-12410" class="comment">
<div id="post-12410-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>help.osm.org is not the best place to ask questions about xslt or other general problems not related to gis. You may find other sites that have more xslt experts than osm, like <a href="http://stackoverflow.com/">http://stackoverflow.com/</a></p>
</div>
<div id="comment-12410-info" class="comment-info">
<span class="comment-age">(28 Apr '12, 19:27)</span> <span class="comment-user userinfo">Gnonthgol ♦</span>
</div>
</div>
</div>
<div id="comment-tools-12409" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12409-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant - This is not an XSLT help forum." by Frederik Ramm 28 Apr '12, 19:44

</div>

</div>

</div>

