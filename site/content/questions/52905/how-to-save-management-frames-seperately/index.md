+++
type = "question"
title = "How to save management frames seperately?"
description = '''I built a WLAN sniffer on a Raspberry Pi using python scripts and tshark. Tshark saves the captures in a ring buffer containing 10 files with a length of i.e. one minute per file (I cannot change that, because of the limited memory on the Pi) and it runs in a seperate thread, which works just fine. ...'''
date = "2016-05-25T04:51:00Z"
lastmod = "2016-06-02T11:34:00Z"
weight = 52905
keywords = [ "seperation", "management", "wlan", "raspberry" ]
aliases = [ "/questions/52905" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to save management frames seperately?](/questions/52905/how-to-save-management-frames-seperately)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52905-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I built a WLAN sniffer on a Raspberry Pi using python scripts and tshark. Tshark saves the captures in a ring buffer containing 10 files with a length of i.e. one minute per file (I cannot change that, because of the limited memory on the Pi) and it runs in a seperate thread, which works just fine.</p><p>My problem is that I need to save all management frames (the ones outside the ring buffer window, too) to decrypt the other packets. I had the idea to analyze a .pcap file when tshark is done writing to it. Is there any way to get the information from tshark, when it moved on to the next file, and then trigger a function to analyse a file, filter out everything that's not management related and save it to a seperate file? All this would then be done in yet another thread, so the GUI does not freeze and tshark does not pause/stop capturing.</p><p>Or is it possible to filter different packet types and write them into two files directly while capturing wihtout losing any of them?</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags">seperation management wlan raspberry</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 May '16, 04:51</strong></p><img src="https://secure.gravatar.com/avatar/0f828b9496db85d7122d09070f208bcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Baumi&#39;s gravatar image" /><p>Baumi<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Baumi has one accepted answer">100%</span></p></div></div><div id="comments-container-52905" class="comments-container"></div><div id="comment-tools-52905" class="comment-tools"></div><div class="clear"></div><div id="comment-52905-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="53137"></span>

<div id="answer-container-53137" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53137-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Found a solution (but instead of parsing the stdout I used a timer). Could you tell me how I can parse the stdout from dumpcap? I googled a few hours but did not find a proper way to do it. To me, the timer seems very inelegeant.</p><p>This part calls the timer and dumpcap and stops it. Dumpcap is stopped by a SIGTERM command.</p><pre><code>    stopFlag = False
    self.checkFrames = TimerThread(stopFlag)
    self.checkFrames.start()

    # run dumpcap
    dumpcap(&quot;-i%s&quot; % self.interface, &quot;-bduration:%s&quot; % str(self.duration), &quot;-bfiles:10&quot;, &quot;-w/home/pi/Desktop/Python/tmp.pcap&quot;, &quot;-I&quot;)

    # stop the timer
    self.checkFrames.setFlag()</code></pre><p>This is the acutal timer/check-for-EAPOL-frame part: class TimerThread(threading.Thread):</p><pre><code>def __init__(self, stopFlag):
    threading.Thread.__init__(self)
    self.stopped = stopFlag
    self.counter = 1
    self.flag = True

# Keep the timer running as long as dumpcap is active
def run(self):
    # sleep a bit, dumpcap needs some time to start
    time.sleep(2)
    while not self.stopped:
        self.checkFrames()
        time.sleep(1)

# get a list of all .pcap files in the current directory and sort them by date
def checkFrames(self):
    list_files = sh.Command(&quot;find&quot;)
    tmp = list(list_files(&quot;/home/pi/Desktop/Python/&quot;, &quot;-name&quot;, &quot;tmp*&quot;))
    tmp.sort()
    files = [item.replace(&quot;\n&quot;, &quot;&quot;) for item in tmp]
    files.reverse()
    # when there are at least 2 files (so that one is not used by dumpcap anymore),
    # check the 2nd newest for EAPOL frames
    if len(files) &gt;= 2:
        file = files[1]
        # exception for first file
        if self.flag:
            self.old_file = file
            self.flag = False
        # only check, if new file was added, then make current file the &quot;old&quot; file
        if file != self.old_file:
            self.newCheck = CheckThread(file, self.counter)
            self.newCheck.start()
            self.old_file = file
            self.counter += 1

# stopping condition (is set after dumpcap is terminated)
def setFlag(self):
    self.stopped = True

# Create a thread to check the 2nd newest file for EAPOL packets
class CheckThread(threading.Thread):

def __init__(self, file, counter):
    threading.Thread.__init__(self)
    self.file = file
    self.outfile = &quot;/home/pi/Desktop/Python/eapol_&quot; + str(counter) + &quot;.pcap&quot;

# filter out EAPOL frames and put them into a seperate file
def run(self):
    tshark = sh.Command(&quot;tshark&quot;)
    tshark(&quot;-r&quot;, self.file, &quot;-Y&quot;, &quot;eapol&quot;, &quot;-w&quot;, self.outfile)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '16, 04:50</strong></p><img src="https://secure.gravatar.com/avatar/0f828b9496db85d7122d09070f208bcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Baumi&#39;s gravatar image" /><p>Baumi<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Baumi has one accepted answer">100%</span></p></div></div><div id="comments-container-53137" class="comments-container"></div><div id="comment-tools-53137" class="comment-tools"></div><div class="clear"></div><div id="comment-53137-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="52909"></span>

<div id="answer-container-52909" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52909-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Note that you should be using dumpcap to do the capturing, tshark retains state and will consume memory and eventually crash. dumpcap takes the same parameters as tshark for interface specification and ring buffers but can't use tshark display filters, only capture filters.</p><p>If you are discarding a capture after 10 minutes it would seem that you don't need most of the content, only the "management frames", is this correct? If so, why don't you set a filter so that you only capture the management frames, rather than attempt to post-process them out of the captures?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 May '16, 06:11</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-52909" class="comments-container"><span id="52911"></span><div id="comment-52911" class="comment"><div id="post-52911-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your response, I will give dumpcap a try, when I find a solution for the management frames.</p><p>The reason I can't only capture management packets is that the sniffer is supposed to be used to debug actual data from other systems in development, the capturing should end, when the user finds an error end presses "Stop". I don't really know what size the ringbuffer will have, or rather need, when the sniffer is ready to be used, it might also be an hour or two. I might even end up limiting it by filesize instead of time, but there is still a risk that the necessary management frames are pushed out of the buffer.</p></div><div id="comment-52911-info" class="comment-info"><span class="comment-age">(25 May '16, 06:37)</span> Baumi</div></div><span id="52912"></span><div id="comment-52912" class="comment"><div id="post-52912-score" class="comment-score">1</div><div class="comment-text"><p>OK, so it seems you have a few tasks:</p><ol><li>Detect that dumpcap\tshark have finished one capture file and switched to another. dumpcap shows the new filename on stdout, tshark doesn't, so parsing dumpcap stdout would seem to a viable way to do this, otherwise you'll have to watch the capture directory for new files.</li><li>Run tshark on the file that the capturing process has just finished with, filtering for management frames into a new capture file.</li><li>Use mergecap to combine the new capture file with the latest management frames and a capture with all your previous management frames into a new file with all the management frames.</li></ol><p>You should also consider other approaches such as other software already out there that might do something similar, or using tshark you might be able to write a dissector or tap in lua or C that would actively write out the management frames to a new capture file as they are received.</p></div><div id="comment-52912-info" class="comment-info"><span class="comment-age">(25 May '16, 07:04)</span> grahamb ♦</div></div><span id="52913"></span><div id="comment-52913" class="comment"><div id="post-52913-score" class="comment-score"></div><div class="comment-text"><p>dumpcap really does seem to be a viable option for this.</p><p>I will try the "dumpcap -&gt; stdout when a new file is started" approach and come back here, when I have some results.</p><p>Thank you for your help!</p></div><div id="comment-52913-info" class="comment-info"><span class="comment-age">(25 May '16, 07:10)</span> Baumi</div></div><span id="53138"></span><div id="comment-53138" class="comment"><div id="post-53138-score" class="comment-score"></div><div class="comment-text"><p>Now we're really veering off-topic for ask Wireshark, but have a look at the Python <a href="https://docs.python.org/2/library/subprocess.html">subprocess</a> module, and a simple (polling) example <a href="http://www.saltycrane.com/blog/2009/10/how-capture-stdout-in-real-time-python/">here</a>.</p></div><div id="comment-53138-info" class="comment-info"><span class="comment-age">(02 Jun '16, 05:01)</span> grahamb ♦</div></div></div><div id="comment-tools-52909" class="comment-tools"></div><div class="clear"></div><div id="comment-52909-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="53152"></span>

<div id="answer-container-53152" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53152-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Is there a reason why you couldn't run two instances of dumpcap, one capturing only management frames and not using a ring buffer, and one capturing the other frames into a ring buffer?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '16, 11:34</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-53152" class="comments-container"></div><div id="comment-tools-53152" class="comment-tools"></div><div class="clear"></div><div id="comment-53152-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

