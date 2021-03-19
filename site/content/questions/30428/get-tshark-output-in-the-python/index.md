+++
type = "question"
title = "Get tshark output in the python"
description = '''I have a command which works great at the terminal: sudo tshark -V -l -i &#x27;any&#x27; -f &#x27;udp port 4729&#x27;  I trying to read the output from my python script: import subprocess import shlex output = subprocess.check_output(shlex.split(&quot;&quot;&quot;sudo tshark -V -l -i &quot;any&quot; -f &#x27;udp port 4729&#x27;&quot;&quot;&quot;)) print output  I rece...'''
date = "2014-03-04T23:25:00Z"
lastmod = "2014-03-06T14:02:00Z"
weight = 30428
keywords = [ "python", "tshark", "subprocess" ]
aliases = [ "/questions/30428" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Get tshark output in the python](/questions/30428/get-tshark-output-in-the-python)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30428-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a command which works great at the terminal:</p><pre><code>sudo tshark -V -l -i &#39;any&#39; -f &#39;udp port 4729&#39;</code></pre><p>I trying to read the output from my python script:</p><pre><code>import subprocess
import shlex
output = subprocess.check_output(shlex.split(&quot;&quot;&quot;sudo tshark -V -l -i &quot;any&quot; -f &#39;udp port 4729&#39;&quot;&quot;&quot;))
print output</code></pre><p>I receives nothing. But when I press ctrl+c, I receives this:</p><pre><code>[email protected]:~/workspace/glade_tests/src$ sudo ./main.py
tshark: Lua: Error during loading:
 [string &quot;/usr/share/wireshark/init.lua&quot;]:45: dofile has been disabled
Running as user &quot;root&quot; and group &quot;root&quot;. This could be dangerous.
Capturing on Pseudo-device that captures on all interfaces
^C164 packets captured
Traceback (most recent call last):
  File &quot;./main.py&quot;, line 84, in &lt;module&gt;
    output = subprocess.check_output(shlex.split(&quot;&quot;&quot;sudo tshark -V -l -i &quot;any&quot; -f &#39;udp port 4729&#39;&quot;&quot;&quot;))
  File &quot;/usr/lib/python2.7/subprocess.py&quot;, line 538, in check_output
    output, unused_err = process.communicate()
  File &quot;/usr/lib/python2.7/subprocess.py&quot;, line 746, in communicate
    stdout = _eintr_retry_call(self.stdout.read)
  File &quot;/usr/lib/python2.7/subprocess.py&quot;, line 478, in _eintr_retry_call
    return func(*args)
KeyboardInterrupt</code></pre><p>As you can see there is the "164 packets captured" line, which means that thark was working. But where is the output of tshark? Can you help me with this?</p><p>Also tried to use it like this:</p><pre><code>import subprocess
command = [&#39;tshark&#39;, &#39;-V&#39;, &#39;-l&#39;, &#39;-i&#39;, &#39;&quot;any&quot;&#39;, &#39;-f&#39;, &#39;&quot;udp port 4729&quot;&#39;]  # the shell command
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None)
output, error = process.communicate()
print output</code></pre><p>I receive the error:</p><pre><code>[email protected]:~/workspace/glade_tests/src$ sudo ./main.py
tshark: Lua: Error during loading:
 [string &quot;/usr/share/wireshark/init.lua&quot;]:45: dofile has been disabled
Running as user &quot;root&quot; and group &quot;root&quot;. This could be dangerous.
Capturing on &quot;any&quot;
tshark: The capture session could not be initiated (No such device exists).
Please check to make sure you have sufficient permissions, and that you have the proper interface or pipe specified.
0 packets captured</code></pre></div><div id="question-tags" class="tags-container tags">python tshark subprocess</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Mar '14, 23:25</strong></p><img src="https://secure.gravatar.com/avatar/db7ee8856e3f9666eb0d38bca267d3ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gooman&#39;s gravatar image" /><p>Gooman<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gooman has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Mar '14, 23:26</p></div></div><div id="comments-container-30428" class="comments-container"></div><div id="comment-tools-30428" class="comment-tools"></div><div class="clear"></div><div id="comment-30428-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30505"></span>

<div id="answer-container-30505" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30505-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>sudo tshark -V -l -i 'any' -f 'udp port 4729'</p></blockquote><p>sudo expects input from STDIN (the password), so you cannot execute that within a script without taking care about that. However: That's more of a Python scripting question and you would get much better answers in a Python forum.</p><p>Furthermore, <a href="http://wiki.wireshark.org/Development/PrivilegeSeparation">you should <strong>not</strong> run tshark as root</a>!</p><p>So, if you run tshark without sudo (aka without root), your script should (basically) work.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '14, 14:02</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-30505" class="comments-container"><span id="30518"></span><div id="comment-30518" class="comment"><div id="post-30518-score" class="comment-score"></div><div class="comment-text"><p>No, it doesn't work without sudo (just in the terminal). It doesn't without sudo because I catch packets from my device which connected to the USB, so Ubunti Linux doesn't give the access to this USB without root rules.</p></div><div id="comment-30518-info" class="comment-info"><span class="comment-age">(06 Mar '14, 20:35)</span> Gooman</div></div><span id="30526"></span><div id="comment-30526" class="comment"><div id="post-30526-score" class="comment-score"></div><div class="comment-text"><p>It will work without root (sudo), if you follow the steps to correctly configure privilege separation.</p><p>See here:</p><blockquote><p><a href="http://ask.wireshark.org/questions/7523/ubuntu-machine-no-interfaces-listed">http://ask.wireshark.org/questions/7523/ubuntu-machine-no-interfaces-listed</a></p></blockquote><p>The important part is "setcap" for dumpcap!</p></div><div id="comment-30526-info" class="comment-info"><span class="comment-age">(07 Mar '14, 01:45)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-30505" class="comment-tools"></div><div class="clear"></div><div id="comment-30505-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

