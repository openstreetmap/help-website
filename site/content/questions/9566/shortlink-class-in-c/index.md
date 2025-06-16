+++
type = "question"
title = "shortlink class in C#"
description = '''Here is they given rub example for this does anyone know about C# implementation Code for encoding &amp;amp; decoding ... Source code for encoding and decoding shortlinks can be found in short_link.rb on git. This is the ruby code used on the website. If anyone has other language implementations, please...'''
date = "2011-12-17T12:22:00Z"
lastmod = "2012-11-19T21:42:00Z"
weight = 9566
keywords = [ "c#", "links" ]
aliases = [ "/questions/9566" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [shortlink class in C#](/questions/9566/shortlink-class-in-c)

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
<span id="post-9566-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9566-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-9566-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Here is they given rub example for this does anyone know about C# implementation</p>
<p>Code for encoding &amp; decoding ...</p>
<p>Source code for encoding and decoding shortlinks can be found in <a href="http://git.openstreetmap.org/?p=rails.git;a=blob_plain;f=lib/short_link.rb;hb=HEAD">short_link.rb</a> on git. This is the ruby code used on the website. If anyone has other language implementations, please feel free to link them here.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-c#" rel="tag" title="see questions tagged &#39;c#&#39;">c#</span> <span class="post-tag tag-link-links" rel="tag" title="see questions tagged &#39;links&#39;">links</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Dec '11, 12:22</strong></p>
<img src="https://secure.gravatar.com/avatar/ea3361edbf842d1496a3795125f588dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OSMUser&#39;s gravatar image" />
<p><span>OSMUser</span><br />
<span class="score" title="9 reputation points">9</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OSMUser has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-9566" class="comments-container">
<span id="9567"></span>
<div id="comment-9567" class="comment">
<div id="post-9567-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I do not want to sound unfriendly here, but looking at the code it seems quite easy. I wonder if someone who is not able to rewrite it within half an hour can use the result...</p>
</div>
<div id="comment-9567-info" class="comment-info">
<span class="comment-age">(17 Dec '11, 17:16)</span> <span class="comment-user userinfo">LM_1</span>
</div>
</div>
</div>
<div id="comment-tools-9566" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9566-form-container" class="comment-form-container">
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

<span id="17814"></span>

<div id="answer-container-17814" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17814-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17814-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17814-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Today I wrote a VB.Net function for decoding an OSM shortlink, based on the Ruby example. This is now part of my map viewer application:<br />
<a href="http://code.google.com/p/vataviamap/" title="VataviaMap"></a><a href="http://code.google.com/p/vataviamap/">http://code.google.com/p/vataviamap/</a><br />
The source file containing this function is available at:<br />
<a href="http://code.google.com/p/vataviamap/source/browse/trunk/VataviaMap/Shared/clsServer.vb" title="Source Code"></a><a href="http://code.google.com/p/vataviamap/source/browse/trunk/VataviaMap/Shared/clsServer.vb">http://code.google.com/p/vataviamap/source/browse/trunk/VataviaMap/Shared/clsServer.vb</a></p>
<pre><code>Private Const OSMshortlinkEncoding As String = &quot;ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_~&quot;
&#10;    &#39;&#39;&#39; &lt;summary&gt;
    &#39;&#39;&#39; Parse an OpenStreetMap shortlink code into Latitude, Longitude and Zoom
    &#39;&#39;&#39; &lt;/summary&gt;
    &#39;&#39;&#39; &lt;param name=&quot;aCode&quot;&gt;OpenStreetMap shortlink code&lt;/param&gt;
    &#39;&#39;&#39; &lt;param name=&quot;aCenterLatitude&quot;&gt;returns latitude at center of area&lt;/param&gt;
    &#39;&#39;&#39; &lt;param name=&quot;aCenterLongitude&quot;&gt;returns longitude at center of area&lt;/param&gt;
    &#39;&#39;&#39; &lt;param name=&quot;aZoom&quot;&gt;returns zoom level&lt;/param&gt;
    &#39;&#39;&#39; &lt;returns&gt;True if link was parsed and reasonable values for the ByRef arguments were found&lt;/returns&gt;
    &#39;&#39;&#39; &lt;remarks&gt;https://help.openstreetmap.org/questions/9566/shortlink-class-in-c&lt;/remarks&gt;
    Private Function ParseOSMshortlink(ByVal aCode As String, _
                                       ByRef aCenterLatitude As Double, _
                                       ByRef aCenterLongitude As Double, _
                                       ByRef aZoom As Integer) As Boolean
        &#39;http://osm.org/go/0MbEUuTq = https://www.openstreetmap.org/?lat=52.50547&amp;lon=13.36932&amp;zoom=16
        Dim x As Long = 0
        Dim y As Long = 0
        Dim z As Long = 0
        Dim z_offset As Long = 0
&#10;        Try
            &#39; replace @ in old shortlinks with ~
            aCode = aCode.Replace(&quot;@&quot;, &quot;~&quot;)
&#10;            For Each ch As Char In aCode.ToCharArray
                Dim t As Integer = OSMshortlinkEncoding.IndexOf(ch)
                If t &lt; 0 Then
                    z_offset -= 1
                Else
                    For index As Integer = 1 To 3
                        x &lt;&lt;= 1
                        If t And 32 Then x += 1
                        t &lt;&lt;= 1
                        y &lt;&lt;= 1
                        If t And 32 Then y += 1
                        t &lt;&lt;= 1
                    Next
                    z += 3
                End If
            Next
            &#39; pack the coordinates out to their original 32 bits.
            x &lt;&lt;= (32 - z)
            y &lt;&lt;= (32 - z)
&#10;            &#39; project the parameters back to their coordinate ranges.
            aCenterLongitude = (x * 360.0 / 2 ^ 32) - 180.0
            aCenterLatitude = (y * 180.0 / 2 ^ 32) - 90.0
            aZoom = z - 8 - (z_offset Mod 3)
            Return aCenterLatitude &gt; -90 AndAlso aCenterLatitude &lt; 90 AndAlso _
                aCenterLongitude &gt;= -180 AndAlso aCenterLongitude &lt;= 180
        Catch
            Return False
        End Try
    End Function</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Nov '12, 21:42</strong></p>
<img src="https://secure.gravatar.com/avatar/b78f9b37dd696d312b45b1477cc298fd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mark%20Gray&#39;s gravatar image" />
<p><span>Mark Gray</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mark Gray has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-17814" class="comments-container">
&#10;</div>
<div id="comment-tools-17814" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17814-form-container" class="comment-form-container">
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

