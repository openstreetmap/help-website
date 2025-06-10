+++
type = "question"
title = "How can I generate a nice looking heatmap from OSM data?"
description = '''I have trouble with finding something that will generate a nice looking heatmap (something like this one: https://commons.wikimedia.org/wiki/File:Amsterdam_heat_map_OSM.png ) For example http://www.websitedev.de/temp/openlayers-heatmap-layer.html and http://gnuplot.sourceforge.net/demo/heatmaps.html...'''
date = "2013-12-17T21:25:00Z"
lastmod = "2013-12-17T23:09:00Z"
weight = 29147
keywords = [ "heatmap", "data", "data_processing", "processing" ]
aliases = [ "/questions/29147" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How can I generate a nice looking heatmap from OSM data?](/questions/29147/how-can-i-generate-a-nice-looking-heatmap-from-osm-data)

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
<span id="post-29147-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29147-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-29147-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have trouble with finding something that will generate a nice looking heatmap (something like this one: <a href="https://commons.wikimedia.org/wiki/File:Amsterdam_heat_map_OSM.png">https://commons.wikimedia.org/wiki/File:Amsterdam_heat_map_OSM.png</a> ) For example <a href="http://www.websitedev.de/temp/openlayers-heatmap-layer.html">http://www.websitedev.de/temp/openlayers-heatmap-layer.html</a> and <a href="http://gnuplot.sourceforge.net/demo/heatmaps.html">http://gnuplot.sourceforge.net/demo/heatmaps.html</a> seem unable to generate nice looking images (or nobody bothered to produce a nice looking example).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-heatmap" rel="tag" title="see questions tagged &#39;heatmap&#39;">heatmap</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-data_processing" rel="tag" title="see questions tagged &#39;data_processing&#39;">data_processing</span> <span class="post-tag tag-link-processing" rel="tag" title="see questions tagged &#39;processing&#39;">processing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Dec '13, 21:25</strong></p>
<img src="https://secure.gravatar.com/avatar/fd2f7303e92334ed1eef75268aed7611?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bulwersator&#39;s gravatar image" />
<p><span>Bulwersator</span><br />
<span class="score" title="468 reputation points">468</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bulwersator has one accepted answer">14%</span></p>
</div>
</div>
<div id="comments-container-29147" class="comments-container">
<span id="29148"></span>
<div id="comment-29148" class="comment">
<div id="post-29148-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can’t you make one or a script based on OSM yourself ? It seems to me that’s not a specific OSM question, besides that you want OSM data as basement. Feel free to do so.</p>
</div>
<div id="comment-29148-info" class="comment-info">
<span class="comment-age">(17 Dec '13, 22:40)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
</div>
<div id="comment-tools-29147" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29147-form-container" class="comment-form-container">
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

<span id="29149"></span>

<div id="answer-container-29149" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29149-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29149-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-29149-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Bulwersator has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>"nice looking" is obviously always a matter of taste, but I gave it a try. Regular gnuplot heatmaps need data on a grid, not a collection of random points. To get around this limitation I convert the data to an analytic expression and then use "splot". So assume that you start with data, that looks like this:</p>
<pre><code>#x y v
3 2 1
5 6 0.2
8 5 0.5</code></pre>
<p>I used to following python script to create a gnuplot script</p>
<pre><code>#!/usr/bin/python
import sys
import os
import csv
&#10;def main(argv):
    # check arguments
    if len(argv) == 0:
            print &quot;Usage: heatmap.py inputfilename&quot;
            sys.exit(1)
&#10;    # find and open input file
    inputfilename = argv[0]
    try:
            inputfile = open(inputfilename)
    except:
            print &quot;Can&#39;t read &quot;+inputfilename
            sys.exit(1)
&#10;    # open output file carefully
    outputfilemode = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    outputdir = os.path.dirname(os.path.abspath(inputfilename))
    outputbasename = os.path.splitext(os.path.basename(inputfilename))[0]
    outputfilename = os.path.join(outputdir, outputbasename+&quot;.gp&quot;)
    try:
            fd = os.open(outputfilename, outputfilemode, 0744)
    except:
            print &quot;Can&#39;t create &quot;+outputfilename
            sys.exit(1)
&#10;    outputfile = os.fdopen(fd, &quot;w&quot;)
&#10;    # write settings to output file
    outputfile.write(&quot;#!/usr/bin/gnuplot\n&quot;)
    outputfile.write(&quot;set terminal pngcairo size 800,600 enhanced\n&quot;)
    outputfile.write(&quot;set output &#39;heatmap.png&#39;\n&quot;)
    outputfile.write(&quot;set palette defined ( 0 &#39;black&#39;, 1 &#39;red&#39;, 2 &#39;yellow&#39;, 2.1 &#39;white&#39; )\n&quot;)
    outputfile.write(&quot;set isosamples 100, 100\n&quot;)
    outputfile.write(&quot;set style function pm3d\n&quot;)
    outputfile.write(&quot;set pm3d map\n&quot;)
    outputfile.write(&quot;unset colorbox\n&quot;)
    outputfile.write(&quot;unset tics\n&quot;)
    outputfile.write(&quot;set format x &#39;&#39;\n&quot;)
    outputfile.write(&quot;set format y &#39;&#39;\n&quot;)
    outputfile.write(&quot;set lmargin at screen 0\n&quot;)
    outputfile.write(&quot;set rmargin at screen 1\n&quot;)
    outputfile.write(&quot;set bmargin at screen 0\n&quot;)
    outputfile.write(&quot;set tmargin at screen 1\n&quot;)
    # intensity of the dot depending on value
    outputfile.write(&quot;w(v)=v\n&quot;)
    # size of the dot depending on value
    outputfile.write(&quot;s(v)=sqrt(v)\n&quot;)
&#10;    # collect points to plot from dat file
    p = []
    dat_xmin = float(&#39;inf&#39;)
    dat_xmax = float(&#39;-inf&#39;)
    dat_ymin = float(&#39;inf&#39;)
    dat_ymax = float(&#39;-inf&#39;)
&#10;    reader = csv.reader(inputfile, delimiter=&quot; &quot;)
    for r in reader:
            if r[0].startswith(&quot;#&quot;):
                    continue
&#10;            x = float(r[0])
            y = float(r[1])
            v = float(r[2])
            dat_xmin = min(dat_xmin, x)
            dat_xmax = max(dat_xmax, x)
            dat_ymin = min(dat_ymin, y)
            dat_ymax = max(dat_ymax, y)
            p.append(&quot;w(&quot;+str(v)+&quot;)/exp(((x-(&quot;+str(x)+&quot;))**2 + (y-(&quot;+str(y)+&quot;))**2)/s(&quot;+str(v)+&quot;))&quot;)
&#10;    #calculate range
    plot_xmin = dat_xmin - 0.2*(dat_xmax - dat_xmin)
    plot_xmax = dat_xmax + 0.2*(dat_xmax - dat_xmin)
    plot_ymin = dat_ymin - 0.2*(dat_ymax - dat_ymin)
    plot_ymax = dat_ymax + 0.2*(dat_ymax - dat_ymin)
&#10;    # write plot command
    outputfile.write(&quot;splot &quot;)
    outputfile.write(&quot;[&quot;+str(plot_xmin)+&quot;:&quot;+str(plot_xmax)+&quot;][&quot;+str(plot_ymin)+&quot;:&quot;+str(plot_ymax)+&quot;] &quot;)
    outputfile.write(&quot;+&quot;.join(p))
    outputfile.write( &quot; notitle\n&quot;)
&#10;    # close output file
    outputfile.close()
&#10;    print &quot;Done. Now run &quot;+outputfilename
&#10;if __name__ == &quot;__main__&quot;:
    main(sys.argv[1:])</code></pre>
<p>Running the resulting gnuplot script generates the following image</p>
<p><img src="http://help.openstreetmap.org/upfiles/heatmap_1.png" alt="alt text" /></p>
<p>Color palette, size, and relative intensity of the dots can be tweaked but this should at least give you an idea how to generate heatmaps.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Dec '13, 23:08</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</img>
</div>
</div>
<div id="comments-container-29149" class="comments-container">
&#10;</div>
<div id="comment-tools-29149" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29149-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29150"></span>

<div id="answer-container-29150" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29150-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29150-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-29150-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>With QGIS and TileMill</p>
<p><a href="https://www.mapbox.com/tilemill/docs/guides/designing-heat-maps/">https://www.mapbox.com/tilemill/docs/guides/designing-heat-maps/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Dec '13, 23:09</strong></p>
<img src="https://secure.gravatar.com/avatar/efa2bd232d1bfd0540fe303e6cba5f64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jfact0ry&#39;s gravatar image" />
<p><span>Jfact0ry</span><br />
<span class="score" title="366 reputation points">366</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jfact0ry has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-29150" class="comments-container">
&#10;</div>
<div id="comment-tools-29150" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29150-form-container" class="comment-form-container">
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

