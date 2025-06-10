+++
type = "question"
title = "[c#] How to calculate route between two points offline?"
description = '''Hi, I&#x27;ve downloaded my regional map from http://download.geofabrik.de/ and now I only want to calculate distance between two point (coordinates) using C# I&#x27;ve read about BruTile and OSM, but I&#x27;ve no found any piece of code which implements my needs. Map Rendering is not necessary for me, duration ei...'''
date = "2015-06-29T10:01:00Z"
lastmod = "2016-04-20T19:22:00Z"
weight = 43835
keywords = [ "c#", "distance", "offline", "routing", "c#.net" ]
aliases = [ "/questions/43835" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [\[c#\] How to calculate route between two points offline?](/questions/43835/c-how-to-calculate-route-between-two-points-offline)

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
<span id="post-43835-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43835-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43835-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I've downloaded my regional map from <a href="http://download.geofabrik.de/">http://download.geofabrik.de/</a> and now I only want to calculate distance between two point (coordinates) using C#</p>
<p>I've read about BruTile and OSM, but I've no found any piece of code which implements my needs.</p>
<p>Map Rendering is not necessary for me, duration either. I mean, input: two coordinates, output: XX KM. That's all.</p>
<p>Could anybody please help me?</p>
<p>Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-c#" rel="tag" title="see questions tagged &#39;c#&#39;">c#</span> <span class="post-tag tag-link-distance" rel="tag" title="see questions tagged &#39;distance&#39;">distance</span> <span class="post-tag tag-link-offline" rel="tag" title="see questions tagged &#39;offline&#39;">offline</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-c#.net" rel="tag" title="see questions tagged &#39;c#.net&#39;">c#.net</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Jun '15, 10:01</strong></p>
<img src="https://secure.gravatar.com/avatar/4d0d01a465818284bd2d9cd38905b402?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="doShare&#39;s gravatar image" />
<p><span>doShare</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="doShare has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Jun '15, 10:15</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-43835" class="comments-container">
<span id="43868"></span>
<div id="comment-43868" class="comment">
<div id="post-43868-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi again,</p>
<p>I've found a solution consisting in import map to mySQL:</p>
<ul>
<li><a href="http://wiki.openstreetmap.org/wiki/Osm.pm">http://wiki.openstreetmap.org/wiki/Osm.pm</a></li>
<li><a href="http://wiki.openstreetmap.org/wiki/OsmDB.pm">http://wiki.openstreetmap.org/wiki/OsmDB.pm</a></li>
</ul>
<p>I also have installed: MySQL and PERL</p>
<p>The instructions are not clear for me...I dont know how to, import my .osm/.osm.bz2 maps into MySQL and, moreover, how to test distances/routes between two coordinates...</p>
<p>I have installed all the packages into Perl Package Manager, but i am not sure that my installation was fine.</p>
<p>Thanks in advance</p>
</div>
<div id="comment-43868-info" class="comment-info">
<span class="comment-age">(30 Jun '15, 16:33)</span> <span class="comment-user userinfo">doShare</span>
</div>
</div>
<span id="43873"></span>
<div id="comment-43873" class="comment">
<div id="post-43873-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's a completely different question. And why would you want to use MySQL instead of PostgreSQL? There are dozens of instructions for how to import OSM data into a PostgreSQL database. Don't choose a different database unless you have very good reasons for this decision.</p>
</div>
<div id="comment-43873-info" class="comment-info">
<span class="comment-age">(30 Jun '15, 20:03)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="43875"></span>
<div id="comment-43875" class="comment">
<div id="post-43875-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks,</p>
<p>Maybe the question sounds different, but my goal is the same: Obtain real distance (route) between two points offline using OSM. Firstly, I've tried with .NET c# but, because the map size (arround 400MB) the solution doesnt work. So, I am trying to obtain results migrating the map into DataBase. I've tried with mySQL because my .NET application runs over MySQL but, if PostgreSQL is easier, I will look for information / how to. Any suggestion?</p>
<p>Thanks in advance</p>
</div>
<div id="comment-43875-info" class="comment-info">
<span class="comment-age">(01 Jul '15, 07:44)</span> <span class="comment-user userinfo">doShare</span>
</div>
</div>
<span id="43876"></span>
<div id="comment-43876" class="comment">
<div id="post-43876-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>If OsmSharp can't handle large maps then you could think about installing a separate routing service, such as <a href="https://wiki.openstreetmap.org/wiki/GraphHopper">GraphHopper</a> or <a href="https://wiki.openstreetmap.org/wiki/Open_Source_Routing_Machine">OSRM</a>.</p>
</div>
<div id="comment-43876-info" class="comment-info">
<span class="comment-age">(01 Jul '15, 08:02)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="43880"></span>
<div id="comment-43880" class="comment not_top_scorer">
<div id="post-43880-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I thought it was Postgis which is Postgres + a GIS extension. The latter provides functionality to work with point, lines and areas.</p>
</div>
<div id="comment-43880-info" class="comment-info">
<span class="comment-age">(01 Jul '15, 12:38)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="43918"></span>
<div id="comment-43918" class="comment">
<div id="post-43918-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thanks for your help. I've implemented my .NET Solution with GraphHopper. Now, I'm looking for an option to avoid running Terminal Cygwin64 permanently (It starts a local map website)</p>
</div>
<div id="comment-43918-info" class="comment-info">
<span class="comment-age">(02 Jul '15, 12:27)</span> <span class="comment-user userinfo">doShare</span>
</div>
</div>
</div>
<div id="comment-tools-43835" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-43835-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="43836"></span>

<div id="answer-container-43836" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43836-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43836-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43836-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Did you already read the <a href="https://wiki.openstreetmap.org/wiki/Routing">routing</a> wiki page? It even mentions some tools for C#, for example <a href="https://wiki.openstreetmap.org/wiki/OsmSharp">OsmSharp</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jun '15, 10:14</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Jun '15, 10:15</strong> </span></p>
</div>
</div>
<div id="comments-container-43836" class="comments-container">
<span id="43837"></span>
<div id="comment-43837" class="comment">
<div id="post-43837-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi,</p>
<p>Now, i am testing <a href="https://github.com/OsmSharp/OsmSharp/wiki/A-getting-started-example">https://github.com/OsmSharp/OsmSharp/wiki/A-getting-started-example</a> but, because my map size is about 500MB it fails (memory exception).</p>
<p>I am also trying "https://github.com/OsmSharp/OsmSharpDataProcessor/wiki" but I can't do anything with it...</p>
</div>
<div id="comment-43837-info" class="comment-info">
<span class="comment-age">(29 Jun '15, 11:02)</span> <span class="comment-user userinfo">doShare</span>
</div>
</div>
</div>
<div id="comment-tools-43836" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43836-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="49306"></span>

<div id="answer-container-49306" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49306-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49306-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-49306-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I was able to get a result in meters from the code below... however, it took 3.5 minutes to calculate the distance between two points that are 12357 meters apart.</p>
<p>I used the osm.pbf for Oklahoma that is 116mb.</p>
<p>Install VS 2012, Install NuGet Extension, Install OSMSharp via NuGet. Start a new windows app for C#:</p>
<pre><code>using OsmSharp.Osm.PBF.Streams;
using OsmSharp.Routing.Osm.Interpreter;
using OsmSharp.Routing.TSP.Genetic;
using OsmSharp.Math.Geo;
using OsmSharp.Routing;
&#10;using System;
using System.IO;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
&#10;namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
&#10;        private void button1_Click(object sender, EventArgs e)
        {
&#10;            var frCoord = new GeoCoordinate(35.5275684, -97.5691736);
            var toCoord = new GeoCoordinate(35.5575105, -97.6740397);
            var f = new FileInfo(&quot;C:\\OSM\\oklahoma-latest\\oklahoma-latest.osm.pbf&quot;).OpenRead();
            var p = new PBFOsmStreamSource(f);
            var ri = new OsmRoutingInterpreter();
&#10;            var router = Router.CreateLiveFrom(p, ri);
&#10;            var resolved1 = router.Resolve(Vehicle.Car, frCoord);
            var resolved2 = router.Resolve(Vehicle.Car, toCoord);
&#10;            var route = router.Calculate(Vehicle.Car, resolved1, resolved2);
&#10;            label1.Text= Convert.ToString(route.TotalDistance);
        }
&#10;
    }
}</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Apr '16, 19:22</strong></p>
<img src="https://secure.gravatar.com/avatar/4b6da62da13bebd16eca37184773fb59?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kttii&#39;s gravatar image" />
<p><span>kttii</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kttii has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Apr '16, 19:36</strong> </span></p>
</div>
</div>
<div id="comments-container-49306" class="comments-container">
&#10;</div>
<div id="comment-tools-49306" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49306-form-container" class="comment-form-container">
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

