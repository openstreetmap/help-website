+++
type = "question"
title = "tshark in subprocess not writing in csv"
description = '''Im using subprocess to use tshark to capture live traffic in python but even though the command-&amp;gt; tshark = subprocess.Popen([TSHARK_PATH, &quot;-i&quot;,INTERFACE_NO,&quot;-T&quot;+&quot;fields&quot;,&quot;-e&quot;,&quot;frame.time&quot;,&quot;-e&quot;,&quot;frame.number&quot;,&quot;-e&quot;,&quot;eth.dst&quot;,&quot;-e&quot;,&quot;ip.src&quot;,&quot;-e&quot;,&quot;ip.dst&quot;,&quot;-E&quot;,&quot;header=y&quot;, &quot;-E&quot;,&quot;separator=&#x27;,&#x27;&quot;,&quot;-E&quot;, &quot;q...'''
date = "2017-06-20T04:39:00Z"
lastmod = "2017-06-20T11:08:00Z"
weight = 62162
keywords = [ "python", "tshark", "subprocess" ]
aliases = [ "/questions/62162" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark in subprocess not writing in csv](/questions/62162/tshark-in-subprocess-not-writing-in-csv)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62162-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62162-score" class="post-score" title="current number of votes">0</div><span id="post-62162-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Im using subprocess to use tshark to capture live traffic in python but even though the command-&gt;</p><pre><code>tshark = subprocess.Popen([TSHARK_PATH, &quot;-i&quot;,INTERFACE_NO,&quot;-T&quot;+&quot;fields&quot;,&quot;-e&quot;,&quot;frame.time&quot;,&quot;-e&quot;,&quot;frame.number&quot;,&quot;-e&quot;,&quot;eth.dst&quot;,&quot;-e&quot;,&quot;ip.src&quot;,&quot;-e&quot;,&quot;ip.dst&quot;,&quot;-E&quot;,&quot;header=y&quot;, &quot;-E&quot;,&quot;separator=&#39;,&#39;&quot;,&quot;-E&quot;, &quot;quote=d&quot; ,&quot;-E&quot;,&quot;occurrence=f&gt;&quot;+OUTPUT_DIR+OUTPUT_FILE_NAME])</code></pre><p>the above code is capturing the traffic but it is not saving in the csv file. Im getting all the paths from a .yml file by following code</p><pre><code>try:
     with open(&#39;configfile.yml&#39;,&#39;r&#39;) as yf:
        allyml=yaml.load(yf)

except FileNotFoundError:
        logging.error(&quot;ERROR:CONFIG FILE DOES NOT EXIST IN THE GIVEN FILE LOCATION&quot;)

for listing in allyml:
     try:
       TSHARK_PATH=allyml[&#39;TSHARK_PATH&#39;]
       READ_CAPTUREFILE=allyml[&#39;READFROM&#39;]
       OUTPUT_FILE_NAME=allyml[&#39;OUTPUT_FILE_NAME&#39;]
       OUTPUT_DIR=allyml[&#39;OUTPUT_DIR&#39;]
       INTERFACE_NO=allyml[&#39;INTERFACE_NO&#39;]
       # Catch all YAMLErrors
     except yaml.YAMLError:
          logging.exception(&quot;ERROR:CONFIG FILE IS NOT CORRECT&quot;)</code></pre><p>And my .yml file looks like this</p><pre><code>#OPTION will choose whether you want to read an existing pcap file(1) or to capture live traffice(2)
OPTION: &quot;1&quot;
#Enter the path where tshark.exe is located
TSHARK_PATH: &quot;C:\\Program Files\\Wireshark\\tshark.exe&quot;
#location of the pcap file to be read
READFROM: &quot;C:\\mycaptures\\maccdc2012_00000.pcap&quot;
#name of the file to output to 
OUTPUT_FILE_NAME : &quot;captured_packets.csv&quot;
#path of the directory to output to
OUTPUT_DIR: &quot;C:\\mycaptures\\&quot;
INTERFACE_NO: 1
#SELECT DISPLAY OR CAPTURE FILTERS (use 
PACKET_FILTER: &quot;ip&quot;
#in kb
OUTPUT_FILE_SIZE_LIMIT: 200</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-subprocess" rel="tag" title="see questions tagged &#39;subprocess&#39;">subprocess</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jun '17, 04:39</strong></p><img src="https://secure.gravatar.com/avatar/87cc9cdbb338bd8869385782e33fb6fb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dr_dr_&#39;s gravatar image" /><p><span>dr_dr_</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dr_dr_ has no accepted answers">0%</span></p></div></div><div id="comments-container-62162" class="comments-container"></div><div id="comment-tools-62162" class="comment-tools"></div><div class="clear"></div><div id="comment-62162-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62180"></span>

<div id="answer-container-62180" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62180-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62180-score" class="post-score" title="current number of votes">0</div><span id="post-62180-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Not really a Wireshark question, more a Python one, but I think that Popen doesn't understand the redirection operator, instead you should set the stdout argument of Popen to a file object Try something like this:</p><pre><code>f = open(os.path.join(OUTPUT_DIR, OUTPUT_FILE_NAME), &quot;w&quot;)
subprocess.Popen([TSHARK COMMAND LINE], stdout = f)
f.close()</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jun '17, 11:08</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-62180" class="comments-container"></div><div id="comment-tools-62180" class="comment-tools"></div><div class="clear"></div><div id="comment-62180-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

